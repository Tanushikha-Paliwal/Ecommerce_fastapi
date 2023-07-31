from tortoise.models import Model
from tortoise import Tortoise,fields

class User(Model):
    id = fields.IntField(pk=True)
    shop_name = fields.CharField(200)
    email = fields.CharField(200,unique=True)
    phone = fields.IntField(10)
    password = fields.CharField(255)
    gst_no = fields.IntField(200)
    is_active = fields.BooleanField(default=True)
    last_login = fields.DatetimeField(auto_now_add=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
