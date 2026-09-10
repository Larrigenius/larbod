from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from config import settings
from routers import contacts


BASE_DIR = Path(__file__).resolve().parent.parent


def create_app(app_settings=settings) -> FastAPI:
    app = FastAPI(
        title=app_settings.app_name,
        docs_url=None if app_settings.is_production else "/docs",
        redoc_url=None if app_settings.is_production else "/redoc",
        openapi_url=None if app_settings.is_production else "/openapi.json",
    )
    
    @app.middleware("http")
    async def add_security_headers(request: Request, call_next):
        response = await call_next(request)

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

        return response

    app.include_router(contacts.router)

    app.mount(
        "/assets",
        StaticFiles(directory=BASE_DIR / "assets"),
        name="assets",
    )

    @app.get("/")
    def home():
        return FileResponse(BASE_DIR / "index.html")

    @app.get("/style.css")
    def style():
        return FileResponse(BASE_DIR / "style.css")

    @app.get("/script.js")
    def script():
        return FileResponse(BASE_DIR / "script.js")

    return app


app = create_app()