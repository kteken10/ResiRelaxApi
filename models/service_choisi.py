from . import db

class ServiceChoisi(db.Model):
    __tablename__ = 'services_choisis'
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    quantite = db.Column(db.Integer, nullable=False)
    reservation = db.relationship('Reservation', back_populates='services_choisis')
    service = db.relationship('Service', back_populates='services_choisis')
