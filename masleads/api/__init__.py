import os

from flask import Flask

from api.elements.resources import ns as elements
from api.extensions import api, db, ma
from api.query_resources import ns as queries


def create_app(testing: bool = False) -> Flask:
    app = Flask(__name__)

    URI_PROD = "postgresql://{}:{}@{}:{}/{}".format(
        os.environ.get("POSTGRES_USER"),
        os.environ.get("POSTGRES_PASSWORD"),
        os.environ.get("POSTGRES_HOST"),
        os.environ.get("POSTGRES_PORT"),
        os.environ.get("POSTGRES_DB"),
    )
    URI = URI_PROD if not testing else str(os.environ.get("DATABASE_URI_TEST"))
    app.config["SQLALCHEMY_DATABASE_URI"] = URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    api.init_app(app)
    ma.init_app(app)

    api.add_namespace(elements)
    api.add_namespace(queries)
    return app
