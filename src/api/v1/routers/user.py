from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.api.v1.schemas import *
from src.api.core.dependencies import UserDep
from src.api.services.user import UserService

router = APIRouter(prefix="/users", tags=["Users", "V1"])
service = UserService()


@router.post("")
async def create_user(schema: UserCreate) -> JSONResponse:
    res = await service.create_user(schema)
    return JSONResponse(**res.response())


@router.get("")
async def get_users() -> JSONResponse:
    res = await service.get_users()
    return JSONResponse(**res.response())


@router.get("/{id}")
async def get_user_by_id(user: UserDep) -> JSONResponse:
    res = await service.get_user(user)
    return JSONResponse(**res.response())


@router.put("/{id}")
async def update_user(user: UserDep, schema: UserUpdate) -> JSONResponse:
    res = await service.update_user(user, schema)
    return JSONResponse(**res.response())


@router.delete("/{id}")
async def delete_user(user: UserDep) -> JSONResponse:
    res = await service.delete_user(user)
    return JSONResponse(**res.response())