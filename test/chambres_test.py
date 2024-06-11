import pytest
import json
from flask_testing import TestCase
from models import db, Chambre
from app import app

class TestChambreResource(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        # Créer un client de test et initialiser la base de données
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    # def test_get_chambres(self):
    #     # Tester l'endpoint pour obtenir la liste des chambres
    #     response = self.client.get('/chambres')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIsInstance(response.json, list)

    def test_post_chambre(self):
        # Ouvrir et charger les données du fichier JSON
        with open('../test/data.json', 'r') as f:
            chambres_data = json.load(f)

        # Parcourir chaque chambre et envoyer une requête POST pour la créer
        for chambre_data in chambres_data:
            # Envoi de la requête POST pour créer une nouvelle chambre
            print(chambre_data)
            response = self.client.post('/chambres', json=chambre_data)
            # Assertions sur la réponse
            self.assertEqual(response.status_code, 201)
            self.assertIn('id', response.json)
            self.assertEqual(response.json['type_chambre'], chambre_data['type_chambre'])

    # def test_get_chambre(self):
    #     # Tester l'endpoint pour obtenir une seule chambre par ID
    #     chambre = Chambre(type_chambre='Double', prix_par_nuit=150.0, active=True, description='Vue sur la montagne', image_path='chemin/image.jpg')
    #     db.session.add(chambre)
    #     db.session.commit()
    #     response = self.client.get(f'/chambres/{chambre.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json['id'], chambre.id)

    # def test_put_chambre(self):
    #     # Tester l'endpoint pour mettre à jour une chambre
    #     chambre = Chambre(type_chambre='Double', prix_par_nuit=15890.0, active=True, description='Vue sur la montagne', image_path='chemin/image.jpg')
    #     db.session.add(chambre)
    #     db.session.commit()
    #     data = {
    #         'type_chambre': 'Suite',
    #         'prix_par_nuit': 200.0,
    #         'active': False,
    #         'description': 'Jacuzzi',
    #         'image_path': 'nouveau_chemin/image.jpg'
    #     }
    #     response = self.client.put(f'/chambres/{chambre.id}', json=data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json['type_chambre'], 'Suite')
    #     self.assertEqual(response.json['prix_par_nuit'], 200.0)
    #     self.assertEqual(response.json['active'], False)
    #     self.assertEqual(response.json['description'], 'Jacuzzi')
    #     self.assertEqual(response.json['image_path'], 'nouveau_chemin/image.jpg')

    # Décommentez et complétez le test pour supprimer une chambre
    # def test_delete_chambre(self):
    #     chambre = Chambre(type_chambre='Double', prix_par_nuit=150.0, active=True, description='Vue sur la montagne', image_path='chemin/image.jpg')
    #     db.session.add(chambre)
    #     db.session.commit()
    #     response = self.client.delete(f'/chambres/{chambre.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json['message'], 'Chambre deleted')

if __name__ == '__main__':
    pytest.main()
