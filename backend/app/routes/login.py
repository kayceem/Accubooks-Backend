from flask import request, render_template, redirect, url_for, flash, get_flashed_messages
from flask.views import MethodView
from .. import schemas
from ..schemas import ValidationError
from ..database import get_db
from .. import models
from werkzeug.security import check_password_hash
from flask_login import login_user


class LoginView(MethodView):
    def get(self):
        return render_template('login.html')

    def post(self):
        form_data = request.form.to_dict()
        user_credentials = None
        try:
            user_credentials = schemas.UserLogin(**form_data)
        except:
            error = 'Invalid information'
        if user_credentials:      
            db = get_db()
            user = db.session.query(models.User).filter(models.User.username == user_credentials.username).first()
            if user is None:
                error = 'Invalid credentials.'
            elif user.password != user_credentials.password:
                error = 'Invalid credentials.'

        if error is None:
            login_user(user)
            return redirect(url_for('dashboard'))
        flash(error)
        return redirect(url_for('login'))