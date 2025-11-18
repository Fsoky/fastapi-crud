import json

from src.db.models import User
from src.db.schemas import UserSchema

from src.core.config import redis_client


async def get_cached_user(id: int) -> User | None:
    """Retrieve a user from Redis cache

    Args:
        id (int): The user ID's

    Returns:
        User | None: Tortoise ORM User instance if found in cache, otherwise None
    """
    
    user_data = await redis_client.get(f"user:{id}")
    if not user_data:
        return None
    return User(**json.loads(user_data))


async def set_cached_user(user: User, *, check: bool = False) -> None:
    """Set a user to Redis cache.

    Args:
        user (User): Tortoise ORM User instance
        check (bool): Whether to check the user in cache. 
            If True and the user is not found in cache, no update will be performed.

    """
    
    user_obj = (
        await UserSchema.from_tortoise_orm(user)
    ).model_dump_json()
    
    if check:
        user_data = await redis_client.get(f"user:{user.id}")
        if not user_data:
            return None
    
    await redis_client.set(f"user:{user.id}", user_obj, 60)
    return None


async def delete_cached_user(user_id: int) -> int:
    return await redis_client.delete(f"user:{user_id}")