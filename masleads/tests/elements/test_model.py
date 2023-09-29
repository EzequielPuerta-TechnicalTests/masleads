from api.elements.model import ElementToProcess

_id = 1
idBulk = 1
retries = 0
status = 20
name = "Element 1"


def test_element_to_process_creation():
    element = ElementToProcess(
        id=_id,
        idBulk=idBulk,
        retries=retries,
        status=status,
        name=name,
    )
    assert element.id == _id
    assert element.idBulk == idBulk
    assert element.retries == retries
    assert element.status == status
    assert element.name == name


def test_element_to_process_representation():
    element = ElementToProcess(
        id=_id,
        idBulk=idBulk,
        retries=retries,
        status=status,
        name=name,
    )
    assert (
        str(element)
        == f"{name} | idBulk: {idBulk} | retries: {retries} | status: {status}"
    )


def test_equality():
    element1 = ElementToProcess(
        id=1,
        idBulk=1,
        retries=0,
        status=20,
        name="Element 1",
    )
    element2 = ElementToProcess(
        id=1,
        idBulk=1,
        retries=0,
        status=20,
        name="Element 1",
    )
    element3 = ElementToProcess(
        id=2,
        idBulk=1,
        retries=0,
        status=20,
        name="Element 1",
    )
    assert element1 == element2
    assert not element1 == element3


def test_hash():
    element1 = ElementToProcess(
        id=1,
        idBulk=1,
        retries=0,
        status=20,
        name="Element 1",
    )
    element2 = ElementToProcess(
        id=1,
        idBulk=1,
        retries=0,
        status=20,
        name="Element 1",
    )
    assert [element1] == [element2]
