from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from my_project.api.dependencies import get_service
from src.my_project.services.service import Service

router = APIRouter(prefix="/")

@router.get("/{item_id:int}")
async def get_feature(
        item_id: int,
        service: Annotated[Service, Depends(get_service)],
):
    return await service.get_data(item_id=item_id)
