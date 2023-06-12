from app.database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    contact_number = db.Column(db.BigInteger, unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
class Product(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=False)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)

class Purchase(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    product_id = db.Column(db.BigInteger, ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)

    product = relationship("Product")

class Sales(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    product_id = db.Column(db.BigInteger, ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)

    product = relationship("Product")
    
