from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True) # Cuz mypy scream error: "User" has no attribute "id"
    created_at = fields.DatetimeField(auto_now_add=True)
    name = fields.CharField(32)
    age = fields.SmallIntField()
    bio = fields.CharField(200)
    
    class Meta:
        table = "users"