from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import File, db
from minio.error import S3Error

files_bp = Blueprint('files', __name__)

@files_bp.route('', methods=['POST'])
@jwt_required()
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    
    user_id = get_jwt_identity()
    filename = file.filename
    file_path = f"user_{user_id}/{filename}"

    try:
        minio_client.put_object(
            "ducks-bucket", file_path, file, length=-1, part_size=10*1024*1024
        )
        new_file = File(name=filename, path=file_path, user_id=user_id)
        db.session.add(new_file)
        db.session.commit()
        return jsonify({"message": "File uploaded successfully", "file_id": new_file.id}), 201
    except S3Error as e:
        return jsonify({"message": f"Error uploading file: {str(e)}"}), 500

@files_bp.route('', methods=['GET'])
@jwt_required()
def list_files():
    user_id = get_jwt_identity()
    files = File.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": f.id, "name": f.name, "tags": [t.name for t in f.tags]} for f in files]), 200
