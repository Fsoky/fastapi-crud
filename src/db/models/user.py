from tortoise import fields
from tortoise.models import Model


class User(Model):
    created_at = fields.DatetimeField(auto_now_add=True)
    name = fields.CharField(32)
    age = fields.SmallIntField()
    bio = fields.CharField(200)
    
    class Meta:
        table = "users"