from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    
    # Relationship with Service
    services = db.relationship('Service', backref='category', lazy=True)

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)  # Optional field for service description
    image_url = db.Column(db.String(255), nullable=True)  # URL to an image for the service
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    # Relationship to ContactForm
    contact_forms = db.relationship('ContactForm', backref='service', lazy=True)

class ContactForm(db.Model):
    __tablename__ = 'contact_forms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)