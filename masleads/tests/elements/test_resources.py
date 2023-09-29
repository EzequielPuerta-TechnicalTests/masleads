from api.elements.schema import element_schema, elements_schema

from ..utils import decode

_id = 1
idBulk = 1
retries = 0
status = 20
name = "Element 1"

element_data = {
    "idBulk": idBulk,
    "retries": retries,
    "status": status,
    "name": name,
}


def test_get_empty_elements(app_client):
    response = app_client.get("/elements/")
    assert response.status_code == 200
    assert decode(response) == []


def test_post_new_element(app_client):
    assert decode(app_client.get("/elements/")) == []
    response = app_client.post("/elements/", json=element_data)
    assert response.status_code == 201
    element = element_schema.load(decode(response))
    assert element.id == 1
    assert element.idBulk == idBulk
    assert element.retries == retries
    assert element.status == status
    assert element.name == name


def test_post_new_element_without_retry(app_client):
    assert decode(app_client.get("/elements/")) == []
    data = {"idBulk": idBulk, "status": status, "name": name}
    response = app_client.post("/elements/", json=data)
    assert response.status_code == 201
    element = element_schema.load(decode(response))
    assert element.id == 1
    assert element.idBulk == idBulk
    assert element.retries is None
    assert element.status == status
    assert element.name == name


def test_get_elements(app_client):
    assert decode(app_client.get("/elements/")) == []
    response = app_client.post("/elements/", json=element_data)
    assert response.status_code == 201
    element = element_schema.load(decode(response))
    response = decode(app_client.get("/elements/"))
    elements = elements_schema.load(response)
    assert elements == [element]


def test_get_one_element(app_client):
    assert decode(app_client.get("/elements/")) == []
    new_element = decode(app_client.post("/elements/", json=element_data))
    new_element = element_schema.load(new_element)
    response = app_client.get(f"/elements/{new_element.id}")
    assert response.status_code == 200
    element = element_schema.load(decode(response))
    assert element.id == new_element.id
    assert element.idBulk == new_element.idBulk
    assert element.retries == new_element.retries
    assert element.status == new_element.status
    assert element.name == new_element.name


def test_get_one_wrong_element(app_client):
    assert decode(app_client.get("/elements/")) == []
    new_element = decode(app_client.post("/elements/", json=element_data))
    new_element = element_schema.load(new_element)
    assert new_element.id == 1
    response = app_client.get("/elements/2")
    assert response.status_code == 404


def test_put_one_element(app_client):
    element = decode(app_client.post("/elements/", json=element_data))
    element = element_schema.load(element)
    assert element.id == 1
    assert element.idBulk == idBulk
    assert element.retries == retries
    assert element.status == status
    assert element.name == name

    response = app_client.put(f"/elements/{element.id}", json={"name": "Eze"})
    new_element = decode(response)
    new_element = element_schema.load(new_element)
    assert element.id == new_element.id
    assert element.idBulk == new_element.idBulk
    assert element.retries == new_element.retries
    assert element.status == new_element.status
    assert not element.name == new_element.name
    assert new_element.name == "Eze"


def test_put_one_wrong_element(app_client):
    assert decode(app_client.get("/elements/")) == []
    response = app_client.put("/elements/1", json={"name": "Eze"})
    assert response.status_code == 404


def test_delete_one_element(app_client):
    assert decode(app_client.get("/elements/")) == []
    element = decode(app_client.post("/elements/", json=element_data))
    assert decode(app_client.get("/elements/")) == [element]
    response = app_client.delete(f"/elements/{element['id']}")
    assert response.status_code == 200
    assert decode(response) == {}
    assert decode(app_client.get("/elements/")) == []


def test_delete_one_wrong_element(app_client):
    assert decode(app_client.get("/elements/")) == []
    element = decode(app_client.post("/elements/", json=element_data))
    assert decode(app_client.get("/elements/")) == [element]
    assert not element["id"] == 2
    response = app_client.delete("/elements/2")
    assert response.status_code == 404
