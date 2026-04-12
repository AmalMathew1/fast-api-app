"""Item repository"""

from app.models.item import Item


_items: dict[int, Item] = {
    1: Item(id=1, name="Apple", price=1.50),
    2: Item(id=2, name="Banana", price=0.75),
}


def get_all() -> list[Item]:
    return list(_items.values())


def get_by_id(item_id: int) -> Item | None:
    return _items.get(item_id)


def create(name: str, price: float) -> Item:
    new_id = max(_items.keys(), default=0) + 1
    new_item = Item(id=new_id, name=name, price=price)
    _items[new_id] = new_item
    return new_item
