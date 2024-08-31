from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from minio import Minio
from .config import Config
from .models import db
from .auth import auth_bp
from .files import files_bp
from .folders import folders_bp
from .tags import tags_bp
from .ponds import ponds_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
Migrate(app, db)
JWTManager(app)

# Initialize Minio client
minio_client = Minio(
    app.config['MINIO_ENDPOINT'],
    access_key=app.config['MINIO_ACCESS_KEY'],
    secret_key=app.config['MINIO_SECRET_KEY'],
    secure=app.config['MINIO_SECURE']
)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(files_bp, url_prefix='/api/files')
app.register_blueprint(folders_bp, url_prefix='/api/folders')
app.register_blueprint(tags_bp, url_prefix='/api/tags')
app.register_blueprint(ponds_bp, url_prefix='/api/ponds')

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "DUCKS is swimming!"}), 200
