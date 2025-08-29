from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str
    age: int
    bio: str


class UserCreate(BaseUser):
    ...


class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    bio: str | None = None


class User(BaseUser):
    id: int