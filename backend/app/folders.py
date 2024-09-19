from flask import Blueprint, request, jsonify
from .models import Folder, db

folders_bp = Blueprint('folders', __name__)

@folders_bp.route('', methods=['POST'])
def create_folder():
    data = request.json
    new_folder = Folder(name=data['name'], parent_id=data.get('parent_id'))
    db.session.add(new_folder)
    db.session.commit()
    return jsonify({"message": "Folder created successfully", "folder_id": new_folder.id}), 201

@folders_bp.route('', methods=['GET'])
def list_folders():
    folders = Folder.query.all()
    return jsonify([{"id": f.id, "name": f.name, "parent_id": f.parent_id} for f in folders]), 200

@folders_bp.route('/<int:folder_id>', methods=['GET'])
def get_folder_contents(folder_id):
    folder = Folder.query.get_or_404(folder_id)
    files = folder.files.all()
    subfolders = folder.children.all()
    return jsonify({
        "files": [{"id": f.id, "name": f.name} for f in files],
        "folders": [{"id": f.id, "name": f.name} for f in subfolders]
    }), 200
