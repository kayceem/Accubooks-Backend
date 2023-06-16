from flask.views import MethodView
from flask_login import login_required
from flask import request, render_template, redirect, url_for
from ..database import get_db
from .. import models



class PurchaseView(MethodView):
    decorators = [login_required]
    def get(self):
        db = get_db()
        purchases = db.session.query(models.Purchase).order_by(models.Purchase.date.desc()).all()
        return render_template('purchase.html', purchases=purchases)

    def post(self):
        pass