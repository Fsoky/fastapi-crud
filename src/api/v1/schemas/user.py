from pydantic import BaseModel, field_validator, Field


class BaseUser(BaseModel):
    name: str
    age: int
    bio: str


class UserCreate(BaseUser):
    
    @field_validator("name")
    @classmethod
    def valid_name(cls, v: str) -> str:
        if len(v) > 32:
            raise ValueError("Name must be less than 32 characters")
        return v
    
    @field_validator("age")
    @classmethod
    def valid_age(cls, v: int) -> int:
        if v > 120:
            raise ValueError("Age must be less than or equal to 120")
        if v <= 0:
            raise ValueError("Age must be greater than 0")
        return v
    
    @field_validator("bio")
    @classmethod
    def valid_bio(cls, v: str) -> str:
        if len(v) > 200:
            raise ValueError("Bio must be less than 200 characters")
        return v


class UserUpdate(BaseModel):
    name: str | None = Field(None, max_length=32)
    age: int | None = Field(None, le=120, gt=0)
    bio: str | None = Field(None, max_length=200)


class UserView(BaseUser):
    id: int