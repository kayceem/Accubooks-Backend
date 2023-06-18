from flask.views import MethodView
from flask import request, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..database import get_db
from .. import models, schemas
from app import bcrypt

class ProfileView(MethodView):
    decorators = [login_required]

    def get(self):
        db = get_db()
        user = db.session.query(models.User).filter(models.User.id==current_user.id).first()
        return render_template('profile.html', user=user)

    def post(self):
        pass