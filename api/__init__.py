from flask_restful import Resource, Api, reqparse
from flask import request, jsonify
from models import Client,Chambre,Reservation,Employe,Service,ServiceChoisi,Image,Paiement
from .client import ClientResource
from .chambre import ChambreResource
from .employe import EmployeResource
from .image import ImageResource
