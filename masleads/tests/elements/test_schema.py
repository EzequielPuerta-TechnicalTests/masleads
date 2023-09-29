from api.elements.model import ElementToProcess
from api.elements.schema import element_schema, elements_schema

_id = 1
idBulk = 1
retries = 0
status = 20
name = "Element 1"


def test_element_to_process_schema_dump() -> None:
    element = ElementToProcess(
        id=_id,
        idBulk=idBulk,
        retries=retries,
        status=status,
        name=name,
    )

    schema = element_schema.dump(element)
    assert isinstance(schema, dict)
    assert schema["id"] == _id
    assert schema["idBulk"] == idBulk
    assert schema["retries"] == retries
    assert schema["status"] == status
    assert schema["name"] == name


def test_elements_to_process_schema_dump() -> None:
    element = ElementToProcess(
        id=_id,
        idBulk=idBulk,
        retries=retries,
        status=status,
        name=name,
    )
    other_element = ElementToProcess(
        id=_id + 1,
        idBulk=idBulk,
        retries=retries,
        status=status,
        name=name,
    )

    schema = elements_schema.dump([element, other_element])
    assert isinstance(schema, list)
    assert schema[0] == element_schema.dump(element)
    assert schema[1] == element_schema.dump(other_element)


def test_element_to_process_schema_load() -> None:
    data = {}
    data["id"] = _id
    data["idBulk"] = idBulk
    data["retries"] = retries
    data["status"] = status
    data["name"] = name

    element = element_schema.load(data)
    assert isinstance(element, ElementToProcess)
    assert element.id == _id
    assert element.idBulk == idBulk
    assert element.retries == retries
    assert element.status == status
    assert element.name == name


def test_elements_to_process_schema_load() -> None:
    raw_elements = [
        {
            "id": _id,
            "idBulk": idBulk,
            "retries": retries,
            "status": status,
            "name": name,
        },
        {
            "id": _id + 1,
            "idBulk": idBulk,
            "retries": retries,
            "status": status,
            "name": name,
        },
    ]

    elements = elements_schema.load(raw_elements)
    element = elements[0]
    assert isinstance(element, ElementToProcess)
    assert element.id == _id
    assert element.idBulk == idBulk
    assert element.retries == retries
    assert element.status == status
    assert element.name == name

    element = elements[1]
    assert isinstance(element, ElementToProcess)
    assert element.id == _id + 1
    assert element.idBulk == idBulk
    assert element.retries == retries
    assert element.status == status
    assert element.name == name
