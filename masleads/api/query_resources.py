from flask_restx import Namespace, Resource, reqparse

from api.elements.model import ElementToProcess
from api.elements.schema import elements_schema

ns = Namespace("queries")


@ns.route("/elements_filter_by_status/<int:status>")
class FilterResource(Resource):
    def get(self, status):  # type: ignore
        elements = ElementToProcess.query.filter_by(status=status)
        for element in elements:
            print(element)
        return elements_schema.dump(elements), 200


parser = reqparse.RequestParser()
parser.add_argument("status", type=int, required=True)
parser.add_argument("id", type=int, required=False)
parser.add_argument("name", type=str, required=False)


@ns.route("/elements_filter_by")
class QueriesResource(Resource):
    @ns.expect(parser)
    def get(self):  # type: ignore
        args = parser.parse_args().items()
        args = {arg: value for arg, value in args if value is not None}
        elements = ElementToProcess.query.filter_by(**args)
        for element in elements:
            print(element)
        return elements_schema.dump(elements), 200
