from flask_restful import Resource, reqparse
from app import db
from models import Chambre

class ChambreResource(Resource):
    def get(self, chambre_id=None):
        if chambre_id:
            chambre = Chambre.query.get(chambre_id)
            if not chambre:
                return {'message': 'Chambre not found'}, 404
            return {
                'id': chambre.id,
                'name': chambre.name,
                'type_chambre': chambre.type_chambre,
                'prix_par_nuit': chambre.prix_par_nuit,
                'active': chambre.active,
                'description': chambre.description,
                'image_path': chambre.image_path
            }
        else:
            chambres = Chambre.query.all()
            return [{
                'id': chambre.id,
                'name': chambre.name,
                'type_chambre': chambre.type_chambre,
                'prix_par_nuit': chambre.prix_par_nuit,
                'active': chambre.active,
                'description': chambre.description,
                'image_path': chambre.image_path
            } for chambre in chambres]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('type_chambre', required=True)
        parser.add_argument('prix_par_nuit', required=True)
        parser.add_argument('active', required=True, type=bool)
        parser.add_argument('description', required=True)
        parser.add_argument('image_path', required=False)
        args = parser.parse_args()

        new_chambre = Chambre(
            name=args['name'],
            type_chambre=args['type_chambre'],
            prix_par_nuit=args['prix_par_nuit'],
            active=args['active'],
            description=args['description'],
            image_path=args.get('image_path')
        )
        db.session.add(new_chambre)
        db.session.commit()
        return {
            'id': new_chambre.id,
            'name': new_chambre.name,
            'type_chambre': new_chambre.type_chambre,
            'prix_par_nuit': new_chambre.prix_par_nuit,
            'active': new_chambre.active,
            'description': new_chambre.description,
            'image_path': new_chambre.image_path
        }, 201

    def put(self, chambre_id):
        chambre = Chambre.query.get(chambre_id)
        if not chambre:
            return {'message': 'Chambre not found'}, 404
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('type_chambre', required=True)
        parser.add_argument('prix_par_nuit', required=True)
        parser.add_argument('active', required=True, type=bool)
        parser.add_argument('description', required=True)
        parser.add_argument('image_path', required=False)
        args = parser.parse_args()

        chambre.name = args['name']
        chambre.type_chambre = args['type_chambre']
        chambre.prix_par_nuit = args['prix_par_nuit']
        chambre.active = args['active']
        chambre.description = args['description']
        chambre.image_path = args.get('image_path')

        db.session.commit()

        return {
            'id': chambre.id,
            'name': chambre.name,
            'type_chambre': chambre.type_chambre,
            'prix_par_nuit': chambre.prix_par_nuit,
            'active': chambre.active,
            'description': chambre.description,
            'image_path': chambre.image_path
        }

    def delete(self, chambre_id):
        chambre = Chambre.query.get(chambre_id)
        if not chambre:
            return {'message': 'Chambre not found'}, 404
        db.session.delete(chambre)
        db.session.commit()
        return {'message': 'Chambre deleted'}
