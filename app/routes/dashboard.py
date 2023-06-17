from flask.views import MethodView
from flask_login import login_required
from flask import request, render_template, redirect, url_for
from ..database import get_db
from .. import models



class DashboardView(MethodView):
    decorators = [login_required]
    def get(self):
        db = get_db()
        products = db.session.query(models.Product).order_by(models.Product.name).all()
        latest_purchases = db.session.query(models.Purchase).order_by(models.Purchase.date.desc(),models.Purchase.id.desc()).limit(10).all()
        latest_sales = db.session.query(models.Sales).order_by(models.Sales.date.desc(), models.Sales.id.desc()).limit(10).all()
        return render_template('dashboard.html', latest_purchases=latest_purchases, latest_sales=latest_sales, products=products)

    def post(self):
        pass