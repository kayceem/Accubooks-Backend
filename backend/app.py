from flask import Flask, request, render_template
from routes.login import LoginView

app = Flask(__name__)
app.add_url_rule('/login', view_func=LoginView.as_view('login'))

if __name__ == '__main__':
    app.run(debug=True)
    