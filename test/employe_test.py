import pytest
from flask_testing import TestCase
from models import db, Employe
from app import app

class TestEmployeResource(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        # Create a test client and initialize the database
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        # Clean up the database after each test
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_employes(self):
        # Test the endpoint to get the list of employees
        response = self.client.get('/employes')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_post_employe(self):
        # Test the endpoint to create a new employee
        data = {
            'nom': 'Doe',
            'prenom': 'John',
            'email': 'john.doe@example.com',
            'telephone': '1234567890',
            'role': 'Manager'
        }
        response = self.client.post('/employes', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['nom'], 'Doe')

    def test_get_employe(self):
        # Test the endpoint to get a single employee by ID
        employe = Employe(nom='Doe', prenom='John', email='john.doe@example.com', telephone='1234567890', role='Manager')
        db.session.add(employe)
        db.session.commit()
        response = self.client.get(f'/employes/{employe.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], employe.id)

    def test_put_employe(self):
        # Test the endpoint to update an employee
        employe = Employe(nom='Doe', prenom='John', email='john.doe@example.com', telephone='1234567890', role='Manager')
        db.session.add(employe)
        db.session.commit()
        data = {
            'nom': 'Smith',
            'prenom': 'Jane',
            'email': 'jane.smith@example.com',
            'telephone': '0987654321',
            'role': 'Receptionist'
        }
        response = self.client.put(f'/employes/{employe.id}', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['nom'], 'Smith')

    def test_delete_employe(self):
        # Test the endpoint to delete an employee
        employe = Employe(nom='Doe', prenom='John', email='john.doe@example.com', telephone='1234567890', role='Manager')
        db.session.add(employe)
        db.session.commit()
        response = self.client.delete(f'/employes/{employe.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Employe deleted')

if __name__ == '__main__':
    pytest.main()
