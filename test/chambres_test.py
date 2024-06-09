import pytest
from flask_testing import TestCase
from models import db, Chambre
from app import app

class TestChambreResource(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        # Create a test client and initialize the database
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    # def tearDown(self):
    #     # Clean up the database after each test
    #     with self.app.app_context():
    #         db.session.remove()
    #         db.drop_all()

    def test_get_chambres(self):
        # Test the endpoint to get the list of rooms
        response = self.client.get('/chambres')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_post_chambre(self):
        # Test the endpoint to create a new room
        data = {
            'type_chambre': 'Single',
            'prix_par_nuit': 100.0,
            'disponibilite': 'Disponible',
            'caracteristiques': 'Vue sur la mer'
        }
        response = self.client.post('/chambres', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['type_chambre'], 'Single')

    def test_get_chambre(self):
        # Test the endpoint to get a single room by ID
        chambre = Chambre(type_chambre='Double', prix_par_nuit=150.0, disponibilite='Disponible', caracteristiques='Vue sur la montagne')
        db.session.add(chambre)
        db.session.commit()
        response = self.client.get(f'/chambres/{chambre.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], chambre.id)

    def test_put_chambre(self):
        # Test the endpoint to update a room
        chambre = Chambre(type_chambre='Double', prix_par_nuit=150.0, disponibilite='Disponible', caracteristiques='Vue sur la montagne')
        db.session.add(chambre)
        db.session.commit()
        data = {
            'type_chambre': 'Suite',
            'prix_par_nuit': 200.0,
            'disponibilite': 'Occupé',
            'caracteristiques': 'Jacuzzi'
        }
        response = self.client.put(f'/chambres/{chambre.id}', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['type_chambre'], 'Suite')

    # def test_delete_chambre(self):
    #     # Test the endpoint to delete a room
    #     chambre = Chambre(type_chambre='Double', prix_par_nuit=150.0, disponibilite='Disponible', caracteristiques='Vue sur la montagne')
    #     db.session.add(chambre)
    #     db.session.commit()
    #     response = self.client.delete(f'/chambres/{chambre.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json['message'], 'Chambre deleted')

if __name__ == '__main__':
    pytest.main()
