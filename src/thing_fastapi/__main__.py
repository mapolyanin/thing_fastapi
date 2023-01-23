import uvicorn

from .services.settings import settings

uvicorn.run(
    "thing_fastapi.app:app",
    host=settings.SERVER_HOST,
    port=settings.SERVER_PORT,
    reload=True,
    log_level="debug",
)

