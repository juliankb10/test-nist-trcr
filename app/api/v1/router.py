from fastapi import APIRouter

from app.api.v1.endpoints import (
    vulnerabilities,
    fixed,
)

from app.api.v1.endpoints import auth

from app.api.v1.endpoints import uploads

api_router = APIRouter()

api_router.include_router(
    auth.router,
    prefix="/v1",
    tags=["Auth"],
)

api_router.include_router(
    vulnerabilities.router,
    prefix="/v1",
    tags=["Vulnerabilities"],
)

api_router.include_router(
    fixed.router,
    prefix="/v1",
    tags=["Fixed"],
)

api_router.include_router(
    uploads.router,
    prefix="/v1",
    tags=["Uploads"],
)