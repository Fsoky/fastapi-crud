from fastapi import APIRouter

from .v1.routers import setup_v1_routers


def setup_routers() -> APIRouter:
    router = APIRouter(prefix="/api")
    
    router.include_router(setup_v1_routers())
    return router