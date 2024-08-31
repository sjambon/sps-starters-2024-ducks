from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .models import Tag, File, db

tags_bp = Blueprint('tags', __name__)

@tags_bp.route('', methods=['POST'])
@jwt_required()
def create_tag():
    data = request.json
    tag = Tag(name=data['name'])
    db.session.add(tag)
    db.session.commit()
    return jsonify({"message": "Tag created successfully", "tag_id": tag.id}), 201

@tags_bp.route('/files/<int:file_id>', methods=['POST'])
@jwt_required()
def add_tag_to_file(file_id):
    data = request.json
    file = File.query.get_or_404(file_id)
    tag = Tag.query.filter_by(name=data['tag_name']).first()
    if not tag:
        tag = Tag(name=data['tag_name'])
        db.session.add(tag)
    file.tags.append(tag)
    db.session.commit()
    return jsonify({"message": "Tag added to file successfully"}), 200