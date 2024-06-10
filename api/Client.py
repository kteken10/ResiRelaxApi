from flask_restful import Resource, reqparse
from flask import jsonify, request
from app import db
from models import Client
import logging

class ClientResource(Resource):
    def get(self, client_id=None):
        if client_id:
            client = Client.query.get(client_id)
            if not client:
                return {'message': 'Client not found'}, 404
            return jsonify({
                'id': client.id,
                'nom': client.nom,
                'prenom': client.prenom,
                'adresse': client.adresse,
                'telephone': client.telephone,
                'email': client.email
            })
        else:
            clients = Client.query.all()
            return jsonify([{
                'id': client.id,
                'nom': client.nom,
                'prenom': client.prenom,
                'adresse': client.adresse,
                'telephone': client.telephone,
                'email': client.email
            } for client in clients])

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('nom', required=True)
            parser.add_argument('prenom', required=True)
            parser.add_argument('adresse', required=False)
            parser.add_argument('email', required=True)
            parser.add_argument('telephone', required=True)
            args = parser.parse_args()

            new_client = Client(
                nom=args['nom'],
                prenom=args['prenom'],
                adresse=args.get('adresse'),
                telephone=args['telephone'],
                email=args['email']
            )
            db.session.add(new_client)
            db.session.commit()
            return jsonify({
                'id': new_client.id,
                'nom': new_client.nom,
                'prenom': new_client.prenom,
                'adresse': new_client.adresse,
                'telephone': new_client.telephone,
                'email': new_client.email
            }), 201
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return {'message': 'An error occurred while creating the client'}, 500

    def put(self, client_id):
        client = Client.query.get(client_id)
        if not client:
            return {'message': 'Client not found'}, 404
        data = request.json
        client.nom = data['nom']
        client.prenom = data['prenom']
        client.adresse = data.get('adresse')
        client.telephone = data.get('telephone')
        client.email = data.get('email')
        db.session.commit()
        return jsonify({
            'id': client.id,
            'nom': client.nom,
            'prenom': client.prenom,
            'adresse': client.adresse,
            'telephone': client.telephone,
            'email': client.email
        })

    def delete(self, client_id):
        client = Client.query.get(client_id)
        if not client:
            return {'message': 'Client not found'}, 404
        db.session.delete(client)
        db.session.commit()
        return {'message': 'Client deleted'}
