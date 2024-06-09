
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __abstract__ = True  
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column('Nom', db.String(100), nullable=False)
    prenom = db.Column('Prénom', db.String(100), nullable=False)
    telephone = db.Column('Téléphone', db.String(20), nullable=True)
    email = db.Column('Email', db.String(100), nullable=True)