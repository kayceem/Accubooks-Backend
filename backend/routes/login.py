from flask.views import MethodView
import schemas
from schemas import ValidationError

class LoginView(MethodView):
    def get(self):
        info ={
            "name":"Kayc",
            "email":"kayc@gmail.com",
            "passwd":"kaycee@logang1",
            "something":"adsaas"
        }
        # Handle the get request here
        try:    
            user= schemas.UserCreate(**info)
            return user.json()
        except ValidationError as e:
            return str(e), 400

    def post(self):
        # Handle the post request here
        return "Handled POST request"