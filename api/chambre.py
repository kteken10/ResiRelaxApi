from . import Resource,jsonify,request,Chambre,reqparse
from app import db
class ChambreResource(Resource):
    def get(self, chambre_id=None):
        if chambre_id:
            chambre = Chambre.query.get(chambre_id)
            if not chambre:
                return {'message': 'Chambre not found'}, 404
            return {
                'id': chambre.id,
                'type_chambre': chambre.type_chambre,
                'prix_par_nuit': chambre.prix_par_nuit,
                'disponibilite': chambre.disponibilite,
                'caracteristiques': chambre.caracteristiques
            }
        else:
            chambres = Chambre.query.all()
            return [{
                'id': chambre.id,
                'type_chambre': chambre.type_chambre,
                'prix_par_nuit': chambre.prix_par_nuit,
                'disponibilite': chambre.disponibilite,
                'caracteristiques': chambre.caracteristiques
            } for chambre in chambres]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type_chambre', required=True)
        parser.add_argument('prix_par_nuit', required=True, type=float)
        parser.add_argument('disponibilite', required=True)
        parser.add_argument('caracteristiques', required=True)
        args = parser.parse_args()

        new_chambre = Chambre(
            type_chambre=args['type_chambre'],
            prix_par_nuit=args['prix_par_nuit'],
            disponibilite=args['disponibilite'],
            caracteristiques=args['caracteristiques']
        )
        db.session.add(new_chambre)
        db.session.commit()
        return {
            'id': new_chambre.id,
            'type_chambre': new_chambre.type_chambre,
            'prix_par_nuit': new_chambre.prix_par_nuit,
            'disponibilite': new_chambre.disponibilite,
            'caracteristiques': new_chambre.caracteristiques
        }, 201
    def put(self, chambre_id):
        chambre = Chambre.query.get(chambre_id)
        if not chambre:
            return {'message': 'Chambre not found'}, 404
        parser = reqparse.RequestParser()
        parser.add_argument('type_chambre', required=True)
        parser.add_argument('prix_par_nuit', required=True, type=float)
        parser.add_argument('disponibilite', required=True)
        parser.add_argument('caracteristiques', required=True)
        args = parser.parse_args()
        chambre.type_chambre = args['type_chambre']
        chambre.prix_par_nuit = args['prix_par_nuit']
        chambre.disponibilite = args['disponibilite']
        chambre.caracteristiques = args['caracteristiques']
        db.session.commit()
        return {
            'id': chambre.id,
            'type_chambre': chambre.type_chambre,
            'prix_par_nuit': chambre.prix_par_nuit,
            'disponibilite': chambre.disponibilite,
            'caracteristiques': chambre.caracteristiques
        }

    def delete(self, chambre_id):
        chambre = Chambre.query.get(chambre_id)
        if not chambre:
            return {'message': 'Chambre not found'}, 404
        db.session.delete(chambre)
        db.session.commit()
        return {'message': 'Chambre deleted'}
