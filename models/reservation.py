from . import db

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    employe_id = db.Column(db.Integer, db.ForeignKey('employes.id'), nullable=False)
    chambre_id = db.Column(db.Integer, db.ForeignKey('chambres.id'), nullable=False)
    date_arrivee = db.Column(db.Date, nullable=False)
    date_depart = db.Column(db.Date, nullable=False)
    statut = db.Column(db.String, nullable=False)
    client = db.relationship('Client', back_populates='reservations')
    employe = db.relationship('Employe', back_populates='reservations')
    chambre = db.relationship('Chambre', back_populates='reservations')
    paiements = db.relationship('Paiement', back_populates='reservation')
    services_choisis = db.relationship('ServiceChoisi', back_populates='reservation')
