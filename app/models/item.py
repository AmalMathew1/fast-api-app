"""Item model"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    id: int
    name: str
    price: float
