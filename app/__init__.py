from flask import Flask

def create_app():
    app = Flask(__name__,
                static_url_path='', 
                static_folder='static',
                template_folder='templates')

    # Load configuration from config.py
    app.config.from_pyfile('../config/config.py')

    # Import and register blueprints (routes)
    from app.routes import heater
    app.register_blueprint(heater.bp)

    return app