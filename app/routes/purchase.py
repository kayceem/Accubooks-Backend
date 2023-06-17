from flask.views import MethodView
from flask_login import login_required
from flask import request, render_template, redirect, url_for
from ..database import get_db
from .. import models
from .. import schemas



class PurchaseView(MethodView):
    decorators = [login_required]
    def get(self):
        db = get_db()
        purchases = db.session.query(models.Purchase).order_by(models.Purchase.date.desc(), models.Purchase.id.desc()).all()
        products = db.session.query(models.Product).order_by(models.Product.name).all()
        return render_template('purchase.html',  purchases=purchases, products=products)

    def post(self):
        db = get_db()
        form_data = request.form.to_dict()
        try:
            purchase = schemas.PurchaseCreate(**form_data)
        except schemas.ValidationError:
            return ({"error": "Invalid information"}), 400
        new_purchase = models.Purchase(
            product_id = purchase.product_id,
            quantity = purchase.quantity,
            date = purchase.date,
            price = purchase.price,
        )
        db.session.add(new_purchase)
        new_product = db.session.query(models.Product).filter(models.Product.id==purchase.product_id).first()
        print(new_product.quantity)
        if new_product:
            new_product.quantity+=purchase.quantity
        db.session.commit()
        return redirect(url_for('purchase'))