from fastapi import FastAPI
from app.routes import main as router

app = FastAPI(title="Load", version="1.1.0")
app.include_router(router.api_router)