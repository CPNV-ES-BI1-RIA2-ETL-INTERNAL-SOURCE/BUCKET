from fastapi import APIRouter

from app.routes import jobs

api_router = APIRouter()

api_router.include_router(jobs.router)