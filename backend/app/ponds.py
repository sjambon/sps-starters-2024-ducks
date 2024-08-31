from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .models import Pond, Tag, File, db

ponds_bp = Blueprint('ponds', __name__)

@ponds_bp.route('', methods=['POST'])
@jwt_required()
def create_pond():
    data = request.json
    pond = Pond(name=data['name'])
    for tag_name in data['tags']:
        tag = Tag.query.filter_by(name=tag_name).first()
        if tag:
            pond.tags.append(tag)
    db.session.add(pond)
    db.session.commit()
    return jsonify({"message": "Pond created successfully", "pond_id": pond.id}), 201

@ponds_bp.route('/<int:pond_id>/files', methods=['GET'])
@jwt_required()
def get_files_in_pond(pond_id):
    pond = Pond.query.get_or_404(pond_id)
    files = File.query.join(File.tags).filter(Tag.id.in_([tag.id for tag in pond.tags])).all()
    return jsonify([{"id": f.id, "name": f.name} for f in files]), 200