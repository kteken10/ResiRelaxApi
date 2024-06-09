from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .client import Client
from .employe import Employe
from .chambre import Chambre
from .image import Image
from .reservation import Reservation
from .paiement import Paiement
from .service import Service
from .service_choisi import ServiceChoisi
