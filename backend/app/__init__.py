from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import settings
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login' 

    from .routes import login, signup, dashboard, search, product, account, purchase, sales, profile, logout
    from . import user_loader 
    app.add_url_rule('/login', view_func=login.LoginView.as_view('login'))
    app.add_url_rule('/signup', view_func=signup.SignupView.as_view('signup'))
    app.add_url_rule('/dashboard', view_func=dashboard.DashboardView.as_view('dashboard'))
    # app.add_url_rule('/search', view_func=search.SearchView.as_view('search'))
    # app.add_url_rule('/product', view_func=product.ProductView.as_view('product'))
    # app.add_url_rule('/account', view_func=account.AccountView.as_view('account'))
    # app.add_url_rule('/purchase', view_func=purchase.PurchaseView.as_view('purchase'))
    # app.add_url_rule('/sales', view_func=sales.SalesView.as_view('sales'))
    # app.add_url_rule('/profile', view_func=profile.ProfileView.as_view('profile'))
    app.add_url_rule('/logout', view_func=logout.LogoutView.as_view('logout'))


    return app
