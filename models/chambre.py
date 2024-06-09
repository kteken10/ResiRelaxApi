from . import db

class Chambre(db.Model):
    __tablename__ = 'chambres'
    id = db.Column(db.Integer, primary_key=True)
    type_chambre = db.Column(db.String, nullable=False)
    prix_par_nuit = db.Column(db.Float, nullable=False)
    disponibilite = db.Column(db.String, nullable=False)
    caracteristiques = db.Column(db.String, nullable=False)
    reservations = db.relationship('Reservation', back_populates='chambre')
    images = db.relationship('Image', back_populates='chambre')
