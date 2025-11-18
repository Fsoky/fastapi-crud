from src.api.core.base_service import BaseService, ServiceResponse
from src.api.v1.schemas import *

from src.db.models import User
from src.db.schemas import UserSchema

from src.core.utils.cache_service import set_cached_user, delete_cached_user


class UserService(BaseService):
    
    async def get_users(self) -> ServiceResponse:
        user_objs = [
            user.model_dump(mode="json", by_alias=True)
            for user in await UserSchema.from_queryset(User.all())
        ]
        return self.ok(user_objs)
    
    async def get_user(self, user: User) -> ServiceResponse:
        user_obj = (
            await UserSchema.from_tortoise_orm(user)
        ).model_dump(mode="json", by_alias=True)
        return self.ok(user_obj)

    async def create_user(self, schema: UserCreate) -> ServiceResponse:
        await User.create(**schema.model_dump())
        return self.ok(message="User successfully created!")
    
    async def update_user(self, user: User, schema: UserUpdate) -> ServiceResponse:
        user.update_from_dict(schema.model_dump(exclude_none=True))
        await user.save()
        
        await set_cached_user(user, check=True) # Update user in cache
        return self.ok(message="User successfully updated!")

    async def delete_user(self, user: User) -> ServiceResponse:
        await delete_cached_user(user.id) # Delete user from cache
        await user.delete()
        return self.ok(message="User successfully deleted!")


user_service = UserService()