from . import db

class Employe(db.Model):
    __tablename__ = 'employes'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    prenom = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    telephone = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    reservations = db.relationship('Reservation', back_populates='employe')
