from fastapi import APIRouter

from app.routes import objects

api_router = APIRouter()

api_router.include_router(objects.router)