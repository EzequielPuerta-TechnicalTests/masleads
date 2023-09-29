from .utils import decode

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


def test_elements_filter_by_status(app_client):
    assert decode(app_client.get("/elements/")) == []
    response_element = app_client.post("/elements/", json=element_data)
    uri = f"/queries/elements_filter_by_status/{status}"
    response_filter = app_client.get(uri)
    assert response_filter.status_code == 200
    assert decode(response_filter) == [decode(response_element)]


def test_elements_filter_by_wrong_status(app_client):
    assert decode(app_client.get("/elements/")) == []
    response_element = app_client.post("/elements/", json=element_data)
    wrong_status = 30
    assert status == decode(response_element)["status"]
    assert not status == wrong_status
    uri = f"/queries/elements_filter_by_status/{wrong_status}"
    response_filter = app_client.get(uri)
    assert response_filter.status_code == 200
    assert decode(response_filter) == []


def test_elements_filter_by_query(app_client):
    assert decode(app_client.get("/elements/")) == []
    response_element = app_client.post("/elements/", json=element_data)
    uri = f"/queries/elements_filter_by?status={status}"
    response_filter = app_client.get(uri)
    assert response_filter.status_code == 200
    assert decode(response_filter) == [decode(response_element)]


def test_elements_filter_by_multiple_queries(app_client):
    assert decode(app_client.get("/elements/")) == []
    response_element = app_client.post("/elements/", json=element_data)
    uri = f"/queries/elements_filter_by?status={status}&id={_id}"
    response_filter = app_client.get(uri)
    assert response_filter.status_code == 200
    assert decode(response_filter) == [decode(response_element)]


def test_elements_filter_by_wrong_query(app_client):
    assert decode(app_client.get("/elements/")) == []
    response_element = app_client.post("/elements/", json=element_data)
    wrong_status = 30
    assert status == decode(response_element)["status"]
    assert not status == wrong_status
    uri = f"/queries/elements_filter_by?status={wrong_status}"
    response_filter = app_client.get(uri)
    assert response_filter.status_code == 200
    assert decode(response_filter) == []
