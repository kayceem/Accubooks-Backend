from flask.views import MethodView
from .. import schemas
from ..schemas import ValidationError


class DashboardView(MethodView):
    def get(self):
        return "Dashboard"