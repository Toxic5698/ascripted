from ninja import ModelSchema, Schema
from client.models import Client


class ClientSchema(ModelSchema):
    class Config:
        model = Client
        model_fields = '__all__'


class NotFoundSchema(Schema):
    message: str
