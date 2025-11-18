from typing import Annotated
from fastapi import Depends

from src.db.models import User
from .utils.funcs import get_user

UserDep = Annotated[User, Depends(get_user)]