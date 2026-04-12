"""Unit tests for item schema validation"""

import pytest
from pydantic import ValidationError
from app.schemas.item_schema import ItemCreateRequest


pytestmark = pytest.mark.unit


def test_valid_item_create_request():
    request = ItemCreateRequest(name="Apple", price=1.50)
    assert request.name == "Apple"
    assert request.price == 1.50


def test_empty_name_is_rejected():
    with pytest.raises(ValidationError):
        ItemCreateRequest(name="", price=1.50)


def test_name_too_long_is_rejected():
    with pytest.raises(ValidationError):
        ItemCreateRequest(name="A" * 101, price=1.50)


def test_negative_price_is_rejected():
    with pytest.raises(ValidationError):
        ItemCreateRequest(name="Apple", price=-1.00)


def test_zero_price_is_rejected():
    with pytest.raises(ValidationError):
        ItemCreateRequest(name="Apple", price=0)


def test_missing_name_is_rejected():
    with pytest.raises(ValidationError):
        ItemCreateRequest(price=1.50)


def test_missing_price_is_rejected():
    with pytest.raises(ValidationError):
        ItemCreateRequest(name="Apple")
