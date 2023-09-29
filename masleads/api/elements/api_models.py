from flask_restx import fields

from api.extensions import api

element_model_post = api.model(
    "ElementToProcessPOST",
    {
        "idBulk": fields.Integer,
        "retries": fields.Integer(required=False),
        "status": fields.Integer,
        "name": fields.String,
    },
)

element_model_put = api.model(
    "ElementToProcessPUT",
    {
        "idBulk": fields.Integer(required=False),
        "retries": fields.Integer(required=False),
        "status": fields.Integer(required=False),
        "name": fields.String(required=False),
    },
)
