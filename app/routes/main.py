from fastapi import APIRouter

from app.routes import objects

api_router = APIRouter(prefix="/api/v2")

api_router.include_router(objects.router)