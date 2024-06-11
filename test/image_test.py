import pytest
from flask_testing import TestCase
from models import db, Image, Chambre
from app import app

class TestImageResource(TestCase):
    def create_app(self):
       
      
        return app

    def setUp(self):
        # Create a test client and initialize the database
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            # Create a sample Chambre for testing
            self.chambre = Chambre(
                type_chambre='Double',
                prix_par_nuit=150.0,
                disponibilite='Disponible',
                caracteristiques='Vue sur la montagne'
            )
            db.session.add(self.chambre)
            db.session.commit()
            db.session.refresh(self.chambre)  # Refresh to ensure the session is aware of the instance

   

    def test_get_images(self):
        # Test the endpoint to get the list of images
        response = self.client.get('/images')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_post_image(self):
        # Test the endpoint to create a new image
        data = {
            'chambre_id': self.chambre.id,
            'url': 'http://example.com/image.jpg'
        }
        response = self.client.post('/images', json=data)
        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response.data.decode('utf-8')}")
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['url'], 'http://example.com/image.jpg')

    def test_get_image(self):
        # Test the endpoint to get a single image by ID
        image = Image(chambre_id=self.chambre.id, url='http://example.com/image.jpg')
        db.session.add(image)
        db.session.commit()
        response = self.client.get(f'/images/{image.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], image.id)

    def test_put_image(self):
        # Test the endpoint to update an image
        image = Image(chambre_id=self.chambre.id, url='http://example.com/image.jpg')
        db.session.add(image)
        db.session.commit()
        data = {
            'chambre_id': self.chambre.id,
            'url': 'http://example.com/updated_image.jpg'
        }
        response = self.client.put(f'/images/{image.id}', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['url'], 'http://example.com/updated_image.jpg')

    def test_delete_image(self):
        # Test the endpoint to delete an image
        image = Image(chambre_id=self.chambre.id, url='http://example.com/image.jpg')
        db.session.add(image)
        db.session.commit()
        response = self.client.delete(f'/images/{image.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Image deleted')

if __name__ == '__main__':
    pytest.main()
