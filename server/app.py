#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import Category, Service, ContactForm

# Views go here!
class ServiceList(Resource):
    def get(self):
        services = Service.query.all()
        return [{'id': service.id, 'name': service.name, 'description': service.description, 'image_url': service.image_url, 'category_id': service.category_id} for service in services]

    def post(self):
        data = request.get_json()
        if 'category_id' not in data:
            return {"message": "Category ID is required."}, 400
        try:
            category = Category.query.filter_by(id=data['category_id']).one()
        except NoResultFound:
            return {"message": "Category not found."}, 404

        new_service = Service(
            name=data['name'],
            description=data['description'],
            image_url=data['image_url'],
            category=category
        )
        db.session.add(new_service)
        db.session.commit()
        return {'id': new_service.id}, 201
    
    def delete(self, id):
        service = Service.query.get_or_404(id)
        db.session.delete(service)
        db.session.commit()
        return {'message': 'Service deleted'}, 200

class ContactFormResource(Resource):
    def post(self):
        data = request.get_json()
        new_contact = ContactForm(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            service_id=data.get('service_id'),  # Ensure this field is optional
            message=data['message']
        )
        db.session.add(new_contact)
        db.session.commit()
        return {'id': new_contact.id}, 201
    
    def delete(self, id):
        contact = ContactForm.query.get_or_404(id)
        db.session.delete(contact)
        db.session.commit()
        return {'message': 'Contact deleted'}, 200
    
class ContactList(Resource):
    def get(self):
        contacts = ContactForm.query.all()
        return [{
            'id': contact.id,
            'name': contact.name,
            'email': contact.email,
            'phone': contact.phone,
            'service_id': contact.service_id,
            'message': contact.message
        } for contact in contacts]
    
class CategoryList(Resource):
    def get(self):
        categories = Category.query.all()
        return [{'id': category.id, 'name': category.name} for category in categories]

    def post(self):
        data = request.get_json()
        new_category = Category(name=data['name'])
        db.session.add(new_category)
        db.session.commit()
        return {'id': new_category.id}, 201

# Register API resources
api.add_resource(ServiceList, '/services')
api.add_resource(ContactFormResource, '/contact')
api.add_resource(ContactList, '/contacts')
api.add_resource(CategoryList, '/categories')

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)

