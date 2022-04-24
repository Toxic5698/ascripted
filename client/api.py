from decimal import Decimal
from typing import List, Optional

from ninja import NinjaAPI

from client.models import Profile
from client.schema import ProfileSchema, NotFoundSchema


api = NinjaAPI()


@api.get("/", response=List[ProfileSchema])
def profile_list(request, name: Optional[str] = None, debt: Optional[bool] = None):
    if name:
        return Profile.objects.filter(name__icontains=name)
    elif debt:
        return Profile.objects.filter(debt__gt=Decimal(1))
    elif not debt:
        return Profile.objects.filter(debt__lt=Decimal(1))
    return Profile.objects.all()


@api.get("/{profile_id}", response={200: ProfileSchema, 404: NotFoundSchema})
def profile_detail(request, profile_id):
    try:
        profile = Profile.objects.get(pk=profile_id)
        return 200, profile
    except Profile.DoesNotExist as e:
        return 404, {"message": "Could not find profile with given attribute."}

