from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import settings
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    db.init_app(app)

    from .routes import login, signup, dashboard, search, product, account, purchase, sales, profile
    
    app.add_url_rule('/login', view_func=login.LoginView.as_view('login'))
    # app.add_url_rule('/signup', view_func=signup.SignupView.as_view('signup'))
    app.add_url_rule('/dashboard', view_func=dashboard.DashboardView.as_view('dashboard'))
    # app.add_url_rule('/search', view_func=search.SearchView.as_view('search'))
    # app.add_url_rule('/product', view_func=product.ProductView.as_view('product'))
    # app.add_url_rule('/account', view_func=account.AccountView.as_view('account'))
    # app.add_url_rule('/purchase', view_func=purchase.PurchaseView.as_view('purchase'))
    # app.add_url_rule('/sales', view_func=sales.SalesView.as_view('sales'))
    # app.add_url_rule('/profile', view_func=profile.ProfileView.as_view('profile'))

    return app
