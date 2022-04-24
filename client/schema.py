from ninja import ModelSchema, Schema
from client.models import Profile


class ProfileSchema(ModelSchema):
    class Config:
        model = Profile
        model_fields = '__all__'


class NotFoundSchema(Schema):
    message: str