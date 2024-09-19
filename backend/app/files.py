from flask import Blueprint, jsonify, request, current_app as app
from .models import File, db
from minio import Minio
from minio.error import S3Error
import io
from datetime import timedelta

files_bp = Blueprint('files', __name__)

# MinIO client initialization inside a function
def get_minio_client():
    return Minio(
        app.config['MINIO_ENDPOINT'],
        access_key=app.config['MINIO_ACCESS_KEY'],
        secret_key=app.config['MINIO_SECRET_KEY'],
        secure=app.config['MINIO_SECURE']
    )

# Ensure the 'ducks' bucket exists, but inside the correct context
@files_bp.before_app_request
def initialize_minio():
    minio_client = get_minio_client()
    try:
        if not minio_client.bucket_exists('ducks'):
            minio_client.make_bucket('ducks')
    except Exception as e:
        app.logger.error(f"Error creating 'ducks' bucket: {str(e)}")


@files_bp.route('', methods=['GET'])
def list_files():
    minio_client = get_minio_client()  # Get the MinIO client within the route
    try:
        files = File.query.all()
        if not files:
            return jsonify({"message": "No files found"}), 200
        file_list = []
        for file in files:
            url = minio_client.presigned_get_object('ducks', file.path, expires=timedelta(hours=1))
            file_list.append({"id": file.id, "name": file.name, "url": url})
        return jsonify(file_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@files_bp.route('/upload', methods=['POST'])
def upload_file():
    minio_client = get_minio_client()
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    try:
        file_data = file.read()
        file_size = len(file_data)
        if file_size == 0:
            return jsonify({"error": "File size is 0 bytes. Cannot upload empty file."}), 400

        file_stream = io.BytesIO(file_data)
        object_name = f"{file.filename}"
        minio_client.put_object(
            'ducks',
            object_name,
            file_stream,
            file_size,
            content_type=file.content_type
        )
        new_file = File(name=file.filename, path=object_name)
        db.session.add(new_file)
        db.session.commit()

        return jsonify({"message": "File uploaded successfully", "file_name": file.filename}), 201
    except S3Error as e:
        return jsonify({"error": f"MinIO S3 error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
