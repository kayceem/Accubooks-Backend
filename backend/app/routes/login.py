from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from flask import request
from .. import schemas
from ..schemas import ValidationError
from ..database import get_db
from .. import models

class LoginView(MethodView):
    def get(self):
        return "OK"

    def post(self):
        return "OK"