from fastapi import FastAPI
from .services.settings import settings
from .api import router

app =  FastAPI(version=settings.API_VERSION)

app.include_router(router)
