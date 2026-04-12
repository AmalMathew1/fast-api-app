"""Integration tests for item router"""

import pytest
from fastapi.testclient import TestClient


pytestmark = pytest.mark.integration


def test_get_all_items_returns_200(client: TestClient):
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2


def test_get_item_by_id_returns_200(client: TestClient):
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Apple"
    assert data["price"] == 1.50


def test_get_item_not_found_returns_404(client: TestClient):
    response = client.get("/items/99")
    assert response.status_code == 404
    assert response.json()["detail"] == "item not found"


def test_create_item_returns_201(client: TestClient):
    response = client.post("/items/", json={"name": "Mango", "price": 2.00})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Mango"
    assert data["price"] == 2.00
    assert "id" in data


def test_create_item_does_not_affect_other_tests(client: TestClient):
    client.post("/items/", json={"name": "Mango", "price": 2.00})
    response = client.get("/items/")
    assert len(response.json()) == 3


def test_create_item_empty_name_returns_422(client: TestClient):
    response = client.post("/items/", json={"name": "", "price": 2.00})
    assert response.status_code == 422


def test_create_item_negative_price_returns_422(client: TestClient):
    response = client.post("/items/", json={"name": "Mango", "price": -1.00})
    assert response.status_code == 422


def test_create_item_missing_fields_returns_422(client: TestClient):
    response = client.post("/items/", json={})
    assert response.status_code == 422
