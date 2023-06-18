from flask.views import MethodView
from flask_login import login_required, current_user
from flask import request, render_template, redirect, url_for
from ..database import get_db
from .. import models



class DashboardView(MethodView):
    decorators = [login_required]
    def get(self):
        db = get_db()
        user = db.session.query(models.User).filter(models.User.id==current_user.id).first()
        products = db.session.query(models.Product).filter(models.Product.user_id==user.id).order_by(models.Product.name).all()
        latest_purchases = db.session.query(models.Purchase).filter(models.Purchase.user_id==user.id).order_by(models.Purchase.date.desc(),models.Purchase.id.desc()).limit(10).all()
        latest_sales = db.session.query(models.Sales).filter(models.Sales.user_id==user.id).order_by(models.Sales.date.desc(), models.Sales.id.desc()).limit(10).all()
        return render_template('dashboard.html', latest_purchases=latest_purchases, latest_sales=latest_sales, products=products)

    def post(self):
        pass