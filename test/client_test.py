import pytest
from flask_testing import TestCase
from models import db, Client
from app import app

class TestClientResource(TestCase):
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

    def test_get_clients(self):
        # Test the endpoint to get the list of clients
        response = self.client.get('/clients')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_post_client(self):
        # Test the endpoint to create a new client
        data = {
            'nom': 'Doe',
            'prenom': 'John',
            'adresse': '123 Main St',
            'email': 'dissangfrancis@yahoo.com',
            'telephone': '1234567890'
        }
        response = self.client.post('/clients', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['nom'], 'Doe')

    def test_get_client(self):
        # Test the endpoint to get a single client by ID
        client = Client(nom='Doe', prenom='John', adresse='123 Main St', email='dissangfrancis@yahoo.com', telephone='1234567890')
        db.session.add(client)
        db.session.commit()
        response = self.client.get(f'/clients/{client.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], client.id)

    def test_put_client(self):
        # Test the endpoint to update a client
        client = Client(nom='Doe', prenom='John', adresse='123 Main St', email='dissangfrancis@yahoo.com', telephone='1234567890')
        db.session.add(client)
        db.session.commit()
        data = {
            'nom': 'Smith',
            'prenom': 'Jane',
            'adresse': '456 Main St',
            'email': 'jane.smith@example.com',
            'telephone': '0987654321'
        }
        response = self.client.put(f'/clients/{client.id}', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['nom'], 'Smith')

    # def test_delete_client(self):
    #     # Test the endpoint to delete a client
    #     client = Client(nom='Doe', prenom='John', adresse='123 Main St', email='dissangfrancis@yahoo.com', telephone='1234567890')
    #     db.session.add(client)
    #     db.session.commit()
    #     response = self.client.delete(f'/clients/{client.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json['message'], 'Client deleted')

if __name__ == '__main__':
    pytest.main()
