from utils.types import ServiceResponse
from utils.schemas import UserCreate, UserUpdate

from db.models import User
from db.schemas import UserSchema


class UserService:
    
    @staticmethod
    async def get_users() -> ServiceResponse:
        user_objs = [
            user.model_dump(mode="json", by_alias=True)
            for user in await UserSchema.from_queryset(User.all())
        ]
        return ServiceResponse(user_objs)
    
    @staticmethod
    async def get_user(id: int) -> ServiceResponse:
        user = await User.filter(id=id).first()
        if not user:
            return ServiceResponse({"error": "User not found"}, 404)
        
        user_obj = (
            await UserSchema.from_tortoise_orm(user)
        ).model_dump(mode="json", by_alias=True)
        return ServiceResponse(user_obj)

    @staticmethod
    async def create_user(user_create: UserCreate) -> ServiceResponse:
        await User.create(**user_create.model_dump())
        return ServiceResponse({"message": "Пользователь создан!"})
    
    @staticmethod
    async def update_user(id: int, user_update: UserUpdate) -> ServiceResponse:
        user = await User.filter(id=id).first()
        if not user:
            return ServiceResponse({"error": "Пользователь не найден"}, 404)
        
        data = user_update.model_dump()
        user.update_from_dict({k: v for k, v in data.items() if v is not None})
        await user.save()
        
        return ServiceResponse({"message": "Пользователь обновлен!"})

    @staticmethod
    async def delete_user(id: int) -> ServiceResponse:
        user = await User.filter(id=id).first()
        if not user:
            return ServiceResponse({"error": "Пользователь не найден"}, 404)
        
        await user.delete()
        return ServiceResponse({"message": "Пользователь удален!"})


user_service = UserService()