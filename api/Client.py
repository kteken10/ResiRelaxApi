from . import Resource,jsonify,request,Client

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
        data = request.json
        new_client = Client(
            nom=data['nom'],
            prenom=data['prenom'],
            adresse=data.get('adresse'),
            telephone=data.get('telephone'),
            email=data.get('email')
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
        })

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
