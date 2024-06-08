import os
import jwt
from jwt import encode as jwt_encode, decode as jwt_decode
from os import environ as env
from dotenv import find_dotenv, load_dotenv
from werkzeug.utils import secure_filename
from flask import Flask,  jsonify, request
from models import db
from flask import send_file
from flask_migrate import Migrate
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError
from config import config
from datetime import datetime, timedelta
app = Flask(__name__)
env_type = 'production'
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
UPLOAD_FOLDER = 'chemin/vers/le/dossier/de/stockage'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
secret_key = "T0pS3cr3tK3y!#"
app.secret_key = secret_key
app.config.from_object(config[env_type])
db.init_app(app)

# Création des tables
with app.app_context():
    db.create_all()
migrate = Migrate(app, db)
CORS(app)  


@app.route('/')
def index():
    return "Votre Application est deployé et fonctionne correctement"


if __name__ == "__main__":
    # app.run()
    # app.run(host='0.0.0.0')
    app.run(port=int(os.environ.get('PORT', 5000)))