from fastapi import APIRouter

from .feature.routes import router as feature_router

router = APIRouter(prefix="v1")
router.include_router(feature_router)