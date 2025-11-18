from fastapi import HTTPException

from src.db.models import User
from src.core.utils.cache_service import get_cached_user, set_cached_user


async def get_user(id: int) -> User:
    user = await get_cached_user(id)
    if not user:
        user = await User.filter(id=id).first()
        if not user:
            raise HTTPException(404, "User not found!")

        await set_cached_user(user)
    return user