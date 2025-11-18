from fastapi import APIRouter

from .import user


def setup_v1_routers() -> APIRouter:
    router = APIRouter(prefix="/v1")
    
    router.include_router(user.router)
    return router