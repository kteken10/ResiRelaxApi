from . import Resource,Employe,reqparse
from app import db
class EmployeResource(Resource):
    def get(self, employe_id=None):
        if employe_id:
            employe = Employe.query.get(employe_id)
            if not employe:
                return {'message': 'Employe not found'}, 404
            return {
                'id': employe.id,
                'nom': employe.nom,
                'prenom': employe.prenom,
                'email': employe.email,
                'telephone': employe.telephone,
                'role': employe.role
            }
        else:
            employes = Employe.query.all()
            return [{
                'id': employe.id,
                'nom': employe.nom,
                'prenom': employe.prenom,
                'email': employe.email,
                'telephone': employe.telephone,
                'role': employe.role
            } for employe in employes]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nom', required=True)
        parser.add_argument('prenom', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('telephone', required=True)
        parser.add_argument('role', required=True)
        args = parser.parse_args()

        new_employe = Employe(
            nom=args['nom'],
            prenom=args['prenom'],
            email=args['email'],
            telephone=args['telephone'],
            role=args['role']
        )
        db.session.add(new_employe)
        db.session.commit()
        return {
            'id': new_employe.id,
            'nom': new_employe.nom,
            'prenom': new_employe.prenom,
            'email': new_employe.email,
            'telephone': new_employe.telephone,
            'role': new_employe.role
        }, 201

    def put(self, employe_id):
        employe = Employe.query.get(employe_id)
        if not employe:
            return {'message': 'Employe not found'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('nom', required=True)
        parser.add_argument('prenom', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('telephone', required=True)
        parser.add_argument('role', required=True)
        args = parser.parse_args()

        employe.nom = args['nom']
        employe.prenom = args['prenom']
        employe.email = args['email']
        employe.telephone = args['telephone']
        employe.role = args['role']
        db.session.commit()
        return {
            'id': employe.id,
            'nom': employe.nom,
            'prenom': employe.prenom,
            'email': employe.email,
            'telephone': employe.telephone,
            'role': employe.role
        }

    def delete(self, employe_id):
        employe = Employe.query.get(employe_id)
        if not employe:
            return {'message': 'Employe not found'}, 404
        db.session.delete(employe)
        db.session.commit()
        return {'message': 'Employe deleted'}