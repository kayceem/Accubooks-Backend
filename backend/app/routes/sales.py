from flask.views import MethodView
from flask_login import login_required
from flask import request, render_template, redirect, url_for
from ..database import get_db
from .. import models
from .. import schemas



class SalesView(MethodView):
    decorators = [login_required]
    def get(self):
        db = get_db()
        sales = db.session.query(models.Sales).order_by(models.Sales.date.desc(), models.Sales.id.desc()).all()
        products = db.session.query(models.Product).order_by(models.Product.name).all()
        return render_template('sales.html',  sales=sales, products=products)

    def post(self):
        db = get_db()
        form_data = request.form.to_dict()
        try:
            sale = schemas.SalesCreate(**form_data)
        except schemas.ValidationError:
            return ({"error": "Invalid information"}), 400
        new_product = db.session.query(models.Product).filter(models.Product.id==sale.product_id).first()

        if not new_product or sale.quantity>new_product.quantity:
            return ({"error": "Not enough quantity"}), 400
            
        new_sale = models.Sales(
            product_id = sale.product_id,
            quantity = sale.quantity,
            date = sale.date,
            price = sale.price,
        )
        db.session.add(new_sale)
        new_product.quantity-=sale.quantity
        db.session.commit()
        return redirect(url_for('sales'))