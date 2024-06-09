from app import db
from . import Resource,jsonify,request,Image,reqparse
class ImageResource(Resource):
    def get(self, image_id=None):
        if image_id:
            image = Image.query.get(image_id)
            if not image:
                return {'message': 'Image not found'}, 404
            return {
                'id': image.id,
                'chambre_id': image.chambre_id,
                'url': image.url
            }
        else:
            images = Image.query.all()
            return [{
                'id': image.id,
                'chambre_id': image.chambre_id,
                'url': image.url
            } for image in images]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('chambre_id', required=True, type=int)
        parser.add_argument('url', required=True)
        args = parser.parse_args()

        new_image = Image(
            chambre_id=args['chambre_id'],
            url=args['url']
        )
        db.session.add(new_image)
        db.session.commit()
        return {
            'id': new_image.id,
            'chambre_id': new_image.chambre_id,
            'url': new_image.url
        }, 201

    def put(self, image_id):
        image = Image.query.get(image_id)
        if not image:
            return {'message': 'Image not found'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('chambre_id', required=True, type=int)
        parser.add_argument('url', required=True)
        args = parser.parse_args()

        image.chambre_id = args['chambre_id']
        image.url = args['url']
        db.session.commit()
        return {
            'id': image.id,
            'chambre_id': image.chambre_id,
            'url': image.url
        }

    def delete(self, image_id):
        image = Image.query.get(image_id)
        if not image:
            return {'message': 'Image not found'}, 404
        db.session.delete(image)
        db.session.commit()
        return {'message': 'Image deleted'}