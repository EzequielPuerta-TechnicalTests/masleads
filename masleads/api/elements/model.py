from api.extensions import db


class ElementToProcess(db.Model):
    __tablename__ = "ElementsToProcess"

    id = db.Column(db.Integer, primary_key=True)
    idBulk = db.Column(db.Integer, nullable=False)
    retries = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return "{} | idBulk: {} | retries: {} | status: {}".format(
            self.name, self.idBulk, self.retries, self.status
        )

    def __eq__(self, value: object) -> bool:
        return isinstance(value, type(self)) and self.id == value.id

    def __hash__(self) -> int:
        return hash((self.id,))
