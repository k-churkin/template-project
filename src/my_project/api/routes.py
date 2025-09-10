"""
Contains API handler functions decorated with FastAPI routes.
"""
from fastapi import APIRouter

from my_project.api.feature.routes import router as feature_router

router = APIRouter(prefix="api")
router.include_router(feature_router)