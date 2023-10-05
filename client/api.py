from decimal import Decimal
from typing import List, Optional

from ninja import NinjaAPI
from ninja.security import django_auth

from client.models import Client
from client.schema import ClientSchema, NotFoundSchema


api = NinjaAPI(csrf=True)


@api.get("/", response=List[ClientSchema], auth=django_auth)
def profile_list(request, name: Optional[str] = None, debt: Optional[bool] = None):
    if name:
        return Client.objects.filter(name__icontains=name)
    elif debt:
        return Client.objects.filter(debt__gt=Decimal(1))
    elif not debt:
        return Client.objects.filter(debt__lt=Decimal(1))
    return Client.objects.all()


@api.get("/{profile_id}", response={200: ClientSchema, 404: NotFoundSchema}, auth=django_auth)
def profile_detail(request, profile_id):
    try:
        profile = Client.objects.get(pk=profile_id)
        return 200, profile
    except Client.DoesNotExist as e:
        return 404, {"message": "Could not find profile with given attribute."}

