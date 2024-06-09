from flask import Flask
from models import db, Client, Employe, Chambre, Image, Reservation, Paiement, Service, ServiceChoisi
import os
from flask_migrate import Migrate
from flask_cors import CORS

from config import config

app = Flask(__name__)
env_type = 'production'
secret_key = "T0pS3cr3tK3y!#"
app.secret_key = secret_key
app.config.from_object(config[env_type])

db.init_app(app)

# Creation des tables
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