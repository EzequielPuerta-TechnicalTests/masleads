import pytest
from flask.testing import FlaskClient

from api import create_app
from api.extensions import db


@pytest.fixture
def app_client() -> FlaskClient:
    _app = create_app(testing=True)

    with _app.app_context():
        db.create_all()

    yield _app.test_client()
    with _app.app_context():
        db.drop_all()
