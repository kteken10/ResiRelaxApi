from . import db

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    prenom = db.Column(db.String, nullable=False)
    adresse = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False, unique=True)
    telephone = db.Column(db.String, nullable=False)
    reservations = db.relationship('Reservation', back_populates='client')
