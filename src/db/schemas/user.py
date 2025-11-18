from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from tortoise.contrib.pydantic import pydantic_model_creator

from src.db.models.user import User

UserSchema = pydantic_model_creator(
    User,
    model_config=ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True
    )
)