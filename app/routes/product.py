from flask.views import MethodView
from flask_login import login_required
from flask import render_template
from ..database import get_db
from .. import models



class ProductView(MethodView):
    decorators = [login_required]
    def get(self, product_id):
        db = get_db()
        product = db.session.query(models.Product).filter(models.Product.id == product_id).first()
        if not product:
                        return ({"error": "Product Not Found"}), 404
        purchases = db.session.query(models.Purchase).filter(models.Purchase.product_id == product.id).order_by(models.Purchase.date.desc()).all()
        sales = db.session.query(models.Sales).filter(models.Sales.product_id == product.id).order_by(models.Sales.date.desc()).all()
        return render_template('product.html', product=product, purchases=purchases, sales= sales)

    def post(self):
        pass