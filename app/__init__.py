from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config



def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(Config)

    Migrate(app)  

    from .routes import bp
    app.register_blueprint(bp)

    return app
