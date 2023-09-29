from typing import Any

from marshmallow import post_load

from api.elements.model import ElementToProcess
from api.extensions import ma


class ElementToProcessSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ElementToProcess
        include_fk = True

    @post_load
    def make(self, data: Any, **kwargs: Any) -> ElementToProcess:
        return ElementToProcess(**data)


element_schema = ElementToProcessSchema()
elements_schema = ElementToProcessSchema(many=True)
