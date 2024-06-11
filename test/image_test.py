import pytest
from flask_testing import TestCase
from models import db, Image, Chambre
from app import app

class TestImageResource(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        # Créer un client de test et initialiser la base de données
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            # Créer une chambre d'échantillon pour les tests
            self.chambre = Chambre(
                type_chambre='Double',
                prix_par_nuit=150.0,
                active=True,
                description='Vue sur la montagne'
            )
            db.session.add(self.chambre)
            db.session.commit()
            db.session.refresh(self.chambre)  # Rafraîchir pour s'assurer que la session est consciente de l'instance

    def test_get_images(self):
        # Tester l'endpoint pour obtenir la liste des images
        response = self.client.get('/images')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_post_image(self):
        # Tester l'endpoint pour créer une nouvelle image
        data = {
            'chambre_id': self.chambre.id,
            'url': 'http://example.com/image.jpg'
        }
        response = self.client.post('/images', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['url'], 'http://example.com/image.jpg')

    def test_get_image(self):
        # Tester l'endpoint pour obtenir une seule image par ID
        image = Image(chambre_id=self.chambre.id, url='http://example.com/image.jpg')
        db.session.add(image)
        db.session.commit()
        response = self.client.get(f'/images/{image.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], image.id)

    def test_put_image(self):
        # Tester l'endpoint pour mettre à jour une image
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
        # Tester l'endpoint pour supprimer une image
        image = Image(chambre_id=self.chambre.id, url='http://example.com/image.jpg')
        db.session.add(image)
        db.session.commit()
        response = self.client.delete(f'/images/{image.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Image deleted')

if __name__ == '__main__':
    pytest.main()
