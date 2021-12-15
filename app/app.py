from flask import Flask
from flask_migrate import Migrate

from .model import configure as db_config
from .serializer import configure as serializer_config
from .masterpieces import bp

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/bookstore.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db_config(app)
    serializer_config(app)

    app.register_blueprint(bp)

    Migrate(app, app.db)
    return app