from flask import Flask,request, jsonify
from models import db, Client, Employe, Chambre, Image, Reservation, Paiement, Service, ServiceChoisi
import os
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_cors import CORS
from api import ClientResource,EmployeResource,ChambreResource,ImageResource

from config import config

app = Flask(__name__)
api = Api(app)
env_type = 'production'
secret_key = "T0pS3cr3tK3y!#"
app.secret_key = secret_key
app.config.from_object(config[env_type])
db.init_app(app)
with app.app_context():
    db.create_all()
migrate = Migrate(app, db)
CORS(app)  
api.add_resource(ClientResource, '/clients', '/clients/<int:client_id>')
api.add_resource(ChambreResource,'/chambres','/chambres/<int:chambre_id>')
api.add_resource(EmployeResource,'/employes','/employes/<int:employe_id>')
api.add_resource(ImageResource, '/images', '/images/<int:image_id>')


@app.route('/')
def index():
    return "Votre Application est deployé et fonctionne correctement"

if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 5000)))