from flask_marshmallow import Marshmallow
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Api(
    version="0.1.0",
    title="MasLeads Challenge API",
    description="API interface for Masleads's challenge",
)
ma = Marshmallow()
