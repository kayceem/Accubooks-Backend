from app import create_app
from app.database import db
from os import system
from fake_data_generator import generate_and_store_fake_data
system('cls')
if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        generate_and_store_fake_data()
    app.run(debug=True)
