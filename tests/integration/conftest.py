"""Integration test configuration and fixtures"""

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.item import Item
import app.repositories.item_repository as item_repository


INITIAL_ITEMS = {
    1: Item(id=1, name="Apple", price=1.50),
    2: Item(id=2, name="Banana", price=0.75),
}


@pytest.fixture
def client():
    item_repository._items = dict(INITIAL_ITEMS)
    return TestClient(app)
