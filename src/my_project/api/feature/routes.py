from fastapi import APIRouter

from .v1.routes import router as v1_router

router = APIRouter(prefix="/feature")
router.include_router(v1_router)
