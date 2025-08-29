from fastapi import APIRouter
from fastapi.responses import JSONResponse

from utils.schemas import UserCreate, UserUpdate

from services.user_service import user_service

router = APIRouter(prefix="/api/users")


@router.post("")
async def create_user(user: UserCreate) -> JSONResponse:
    res = await user_service.create_user(user)
    return JSONResponse(res.data, res.status)


@router.get("")
async def get_users() -> JSONResponse:
    res = await user_service.get_users()
    return JSONResponse(res.data, res.status)


@router.get("/{id}")
async def get_user_by_id(id: int) -> JSONResponse:
    res = await user_service.get_user(id)
    return JSONResponse(res.data, res.status)


@router.put("/{id}")
async def update_user(id: int, user: UserUpdate) -> JSONResponse:
    res = await user_service.update_user(id, user)
    return JSONResponse(res.data, res.status)


@router.delete("/{id}")
async def delete_user(id: int) -> JSONResponse:
    res = await user_service.delete_user(id)
    return JSONResponse(res.data, res.status)