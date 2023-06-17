from faker import Faker
from sqlalchemy.orm import Session
from app import db
from app.models import Product, Purchase, Sales
import random

# Create a Faker instance
fake = Faker()

# Define a function to create fake products
def create_fake_products(n=20):
    products = []
    for i in range(n):
        product = Product(
            name=fake.word(),
            quantity=fake.random_int(min=0, max=500),
        )
        products.append(product)
    return products

# Define a function to create fake purchases and sales
def create_fake_purchases_and_sales(products, n=50):
    purchases = []
    sales = []
    for _ in range(n):
        product = random.choice(products)
        quantity = fake.random_int(min=1, max=100)
        price = fake.random_int(min=1, max=500)
        date = fake.date_between(start_date='-1y', end_date='today')
        pid = fake.random_int(min=1, max=20)
        purchase = Purchase(
            product_id=pid,
            quantity=quantity,
            price=price,
            date=date,
            product=product
        )
        sale = Sales(
            product_id=pid,
            quantity=quantity-pid if quantity>pid else pid-quantity,
            price=price+pid*2,
            date=date,
            product=product
        )

        purchases.append(purchase)
        sales.append(sale)
    return purchases, sales


# Define a function to generate and store the fake data
def generate_and_store_fake_data():
    products = create_fake_products(n=20)
    purchases, sales = create_fake_purchases_and_sales(products, n=50)

    # Store the data in the database
    db.session.add_all(products)
    db.session.add_all(purchases)
    db.session.add_all(sales)
    db.session.commit()

from app import create_app
from app.database import db
app = create_app()
with app.app_context():
    db.create_all()
    generate_and_store_fake_data()