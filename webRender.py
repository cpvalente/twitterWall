from flask import Flask
from home.views import web_app


def create_app():

    app = Flask(__name__)  # Create application object
    app.register_blueprint(web_app)  # Register url's so application knows what to do

    return app
