from fastapi import APIRouter

from . import user


def setup_routers() -> APIRouter:
    router = APIRouter()
    
    router.include_router(user.router)
    return router