"""Unit tests for item service"""

import pytest
from unittest.mock import patch
from app.models.item import Item
from app.schemas.item_schema import ItemCreateRequest
from app.services import item_services


pytestmark = pytest.mark.unit


def test_get_all_items_returns_list():
    mock_items = [
        Item(id=1, name="Apple", price=1.50),
        Item(id=2, name="Banana", price=0.75),
    ]
    with patch("app.services.item_services.item_repository.get_all", return_value=mock_items) as mock:
        result = item_services.get_all_items()
        mock.assert_called_once_with()
        assert len(result) == 2
        assert result[0].name == "Apple"


def test_get_item_returns_item_when_found():
    mock_item = Item(id=1, name="Apple", price=1.50)
    with patch("app.services.item_services.item_repository.get_by_id", return_value=mock_item) as mock:
        result = item_services.get_item(1)
        mock.assert_called_once_with(1)
        assert result is not None
        assert result.id == 1
        assert result.name == "Apple"


def test_get_item_returns_none_when_not_found():
    with patch("app.services.item_services.item_repository.get_by_id", return_value=None) as mock:
        result = item_services.get_item(99)
        mock.assert_called_once_with(99)
        assert result is None


def test_create_item_returns_created_item():
    request = ItemCreateRequest(name="Mango", price=2.00)
    mock_created = Item(id=3, name="Mango", price=2.00)
    with patch("app.services.item_services.item_repository.create", return_value=mock_created) as mock:
        result = item_services.create_item(request)
        mock.assert_called_once_with(name="Mango", price=2.00)
        assert result.id == 3
        assert result.name == "Mango"
        assert result.price == 2.00
