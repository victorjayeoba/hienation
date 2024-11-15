from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Set the secret key for sessions and flash messages
    app.config['SECRET_KEY'] = os.urandom(24)  # Secure secret key for the app

    # Import routes
    from . import app as routes
    app.register_blueprint(routes.bp)  # Register the blueprint for routes

    return app
