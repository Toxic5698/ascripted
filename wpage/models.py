from django.db import models
from django.utils.translation import gettext_lazy as _


class OfficeInfo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("name"))
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("address"))
    phone_number = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("phone number"))
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("email"))
    id_number = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("ID number"))
    registration_number = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("registration number"))

    class Meta:
        verbose_name = _("Office info")
        verbose_name_plural = _("Office info")


class WebpageContent(models.Model):
    motto = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("motto"))
    description = models.CharField(max_length=10000, blank=True, null=True, verbose_name=_("description"))
    favicon
    background_image





