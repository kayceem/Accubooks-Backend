from flask.views import MethodView
from flask_login import login_required
from flask import session, render_template
from ..database import get_db
from .. import models
import datetime
from sqlalchemy import extract



class AccountView(MethodView):
    decorators = [login_required]
    def get(self, month=None, year=None):
        if not month or not year:
            now = datetime.datetime.now()
            month = now.month
            year = now.year
        month=int(month)
        year=int(year)
        db = get_db()
        monthly_purchases = db.session.query(models.Purchase).filter(extract('month', models.Purchase.date) == month, extract('year', models.Purchase.date) == year).order_by(models.Purchase.date.desc(), models.Purchase.id.desc()).all()
        monthly_sales = db.session.query(models.Sales).filter(extract('month', models.Sales.date) == month, extract('year', models.Sales.date) == year).order_by(models.Sales.date.desc(), models.Sales.id.desc()).all()
        total_purchase_cost = sum([purchase.price * purchase.quantity for purchase in monthly_purchases])
        total_sales_income = sum([sale.price * sale.quantity for sale in monthly_sales])
        session['month'] = month 
        session['year'] = year
        return render_template('account.html', monthly_purchases=monthly_purchases, monthly_sales=monthly_sales, expenditure= total_purchase_cost, income = total_sales_income)

    def post(self):
        pass