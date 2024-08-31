from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import Folder, db

folders_bp = Blueprint('folders', __name__)

@folders_bp.route('', methods=['POST'])
@jwt_required()
def create_folder():
    data = request.json
    user_id = get_jwt_identity()
    new_folder = Folder(name=data['name'], parent_id=data.get('parent_id'), user_id=user_id)
    db.session.add(new_folder)
    db.session.commit()
    return jsonify({"message": "Folder created successfully", "folder_id": new_folder.id}), 201

@folders_bp.route('', methods=['GET'])
@jwt_required()
def list_folders():
    user_id = get_jwt_identity()
    folders = Folder.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": f.id, "name": f.name, "parent_id": f.parent_id} for f in folders]), 200

@folders_bp.route('/<int:folder_id>', methods=['GET'])
@jwt_required()
def get_folder_contents(folder_id):
    folder = Folder.query.get_or_404(folder_id)
    files = folder.files.all()
    subfolders = folder.children.all()
    return jsonify({
        "files": [{"id": f.id, "name": f.name} for f in files],
        "folders": [{"id": f.id, "name": f.name} for f in subfolders]
    }), 200