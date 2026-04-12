"""Item router"""

from fastapi import APIRouter, HTTPException
from app.services import item_services
from app.schemas.item_schema import ItemCreateRequest, ItemResponse


router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.get("/", response_model=list[ItemResponse])
def get_all_items() -> list[ItemResponse]:
    return item_services.get_all_items()


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int) -> ItemResponse:
    item = item_services.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item


@router.post("/", status_code=201, response_model=ItemResponse)
def create_item(request: ItemCreateRequest) -> ItemResponse:
    return item_services.create_item(request)
