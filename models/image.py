from . import db

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    chambre_id = db.Column(db.Integer, db.ForeignKey('chambres.id'), nullable=False)
    url = db.Column(db.String, nullable=False)
    chambre = db.relationship('Chambre', back_populates='images')
