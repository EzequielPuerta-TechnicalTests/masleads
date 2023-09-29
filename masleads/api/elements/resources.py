from flask_restx import Namespace, Resource, abort

from api.elements.api_models import element_model_post, element_model_put
from api.elements.model import ElementToProcess
from api.elements.schema import element_schema, elements_schema
from api.extensions import db

ns = Namespace("elements")


@ns.route("/")
class ElementsToProcessResource(Resource):
    def get(self):  # type: ignore
        return elements_schema.dump(ElementToProcess.query.all())

    @ns.expect(element_model_post)
    def post(self):  # type: ignore
        element = element_schema.load(ns.payload)
        db.session.add(element)
        db.session.commit()
        return element_schema.dump(element), 201


@ns.route("/<int:id>")
class ElementToProcessResource(Resource):
    def get(self, id):  # type: ignore
        element = ElementToProcess.query.get(id)
        if element:
            return element_schema.dump(element), 200
        else:
            return abort(404, "Element to process not found")

    @ns.expect(element_model_put)
    def put(self, id):  # type: ignore
        element = ElementToProcess.query.get(id)
        if element:
            for attribute, value in ns.payload.items():
                setattr(element, attribute, value)
            db.session.commit()
            return element_schema.dump(element), 200
        else:
            return abort(404, "Element to process not found.")

    def delete(self, id):  # type: ignore
        element = ElementToProcess.query.get(id)
        if element:
            db.session.delete(element)
            db.session.commit()
            return {}, 200
        else:
            return abort(404, "Element to process not found.")
