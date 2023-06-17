from flask.views import MethodView
from flask_login import login_required
from flask import request, render_template, redirect, url_for
from ..database import get_db
from .. import models
from .. import schemas



class ProductsView(MethodView):
    decorators = [login_required]
    def get(self):
        db = get_db()
        products = db.session.query(models.Product).order_by(models.Product.name).all()
        return render_template('products.html', products=products)

    def post(self):
        db = get_db()
        form_data = request.form.to_dict()
        try:
            product = schemas.Product(**form_data)
        except schemas.ValidationError:
            return ({"error": "Invalid information"}), 400
        product_exists = db.session.query(models.Product).filter(models.Product.name==product.name).first()

        if product_exists:
            return ({"error": "Product already exists"}), 400
            
        new_product = models.Product(
            name = product.name
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('products'))