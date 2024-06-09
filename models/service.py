from . import db

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    prix = db.Column(db.Float, nullable=False)
    services_choisis = db.relationship('ServiceChoisi', back_populates='service')
