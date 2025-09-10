"""
Contains API handler functions decorated with FastAPI routes.
"""
from fastapi import APIRouter

from .v1.routes import router as api_router

router = APIRouter(prefix="api")
router.include_router(api_router)