from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes
    from . import app as routes
    app.register_blueprint(routes.bp)  # Register the blueprint for routes

    return app
