from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    prenom = db.Column(db.String, nullable=False)
    adresse = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    telephone = db.Column(db.String, nullable=False)
    reservations = db.relationship('Reservation', back_populates='client')

class Employe(db.Model):
    __tablename__ = 'employes'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    prenom = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    telephone = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    reservations = db.relationship('Reservation', back_populates='employe')

class Chambre(db.Model):
    __tablename__ = 'chambres'
    id = db.Column(db.Integer, primary_key=True)
    type_chambre = db.Column(db.String, nullable=False)
    prix_par_nuit = db.Column(db.Float, nullable=False)
    disponibilite = db.Column(db.String, nullable=False)
    caracteristiques = db.Column(db.String, nullable=False)
    reservations = db.relationship('Reservation', back_populates='chambre')

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    chambre_id = db.Column(db.Integer, db.ForeignKey('chambres.id'), nullable=False)
    url = db.Column(db.String, nullable=False)
    chambre = db.relationship('Chambre', back_populates='images')

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

class Paiement(db.Model):
    __tablename__ = 'paiements'
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'), nullable=False)
    montant = db.Column(db.Float, nullable=False)
    date_paiement = db.Column(db.Date, nullable=False)
    methode_paiement = db.Column(db.String, nullable=False)
    reservation = db.relationship('Reservation', back_populates='paiements')

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    prix = db.Column(db.Float, nullable=False)
    services_choisis = db.relationship('ServiceChoisi', back_populates='service')

class ServiceChoisi(db.Model):
    __tablename__ = 'services_choisis'
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    quantite = db.Column(db.Integer, nullable=False)
    reservation = db.relationship('Reservation', back_populates='services_choisis')
    service = db.relationship('Service', back_populates='services_choisis')
