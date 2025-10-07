from email.policy import default
from tabnanny import verbose

from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.fields import BooleanField


# Create your models here.

# ================
#1. Lookup tables (static dictionaries )
#    These entities hold standard classification and names
# ===============

class Manufacturer(models.Model):
    """The core entity for the Pharmaceutical company that produce the drug """
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Manufacturer name"))
    is_active= models.BooleanField(default= True, verbose_name= _("Is active "))

    class Meta:
        verbose_name= _("Manufacturer")
        verbose_name_plural=_("Manufacturers")


