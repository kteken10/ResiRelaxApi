from . import db

class Paiement(db.Model):
    __tablename__ = 'paiements'
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'), nullable=False)
    montant = db.Column(db.Float, nullable=False)
    date_paiement = db.Column(db.Date, nullable=False)
    methode_paiement = db.Column(db.String, nullable=False)
    reservation = db.relationship('Reservation', back_populates='paiements')
