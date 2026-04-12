"""Item service"""

import logging
from app.models.item import Item
from app.schemas.item_schema import ItemCreateRequest
from app.repositories import item_repository

logger = logging.getLogger(__name__)


def get_all_items() -> list[Item]:
    return item_repository.get_all()


def get_item(item_id: int) -> Item | None:
    item = item_repository.get_by_id(item_id)
    if item is None:
        logger.warning("Item not found: id=%s", item_id)
    return item


def create_item(request: ItemCreateRequest) -> Item:
    item = item_repository.create(name=request.name, price=request.price)
    logger.info("Item created: id=%s name=%s", item.id, item.name)
    return item
