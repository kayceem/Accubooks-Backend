from flask import request, render_template, redirect, url_for, jsonify
from flask.views import MethodView
from .. import schemas
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
        except schemas.ValidationError:
            return jsonify({"error": "Invalid information"}), 400

        db = get_db()
        user = db.session.query(models.User).filter(models.User.username == user_credentials.username).first()
        # implement hash checkingh
        if user is None or not (user.password==user_credentials.password):
            return jsonify({"error": "Invalid credentials"}), 401

        login_user(user)
        return redirect(url_for('dashboard'))
