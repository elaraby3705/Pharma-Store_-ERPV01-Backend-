from email.policy import default
from tabnanny import verbose

from django.db import models
from django.utils.module_loading import module_has_submodule
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

    def __str__(self):
        return self.name


class DosageFrom(models.Model):
    """ The Physical form of the medicine (e.g, Tablets, Syrup, Capsule).
    Used for filtering and defining Product Variants . """
    name= models.CharField(max_length=100, unique=True, verbose_name=_("Dosage Form"))

    class Meta:
        verbose_name = _("Dosage Form")
        verbose_name_plural= _("Dosage Forms ")

    def __str__(self):
        return self.name

class ActiveIngredient(models.Model):
    """The chemical responsible for the therapeutic effect (e.g, Paracetamol)
    Crucial for search functionality by the chemical name .
    """
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Active Ingredient"))

    class Meta:
        verbose_name= _("Active Ingredient")
        verbose_name_plural = _("Active Ingredients")

    def __str__(self):
        return self.name

class ATCClass(models.Model):
    """Who's Anatomical Therapeutic chemical (ATC) classification systems (optional)  """
    code = models.CharField(max_length=10, unique=True ,verbose_name= _("ATC code "))
    name= models.CharField(max_length=255, verbose_name=_("ATC Classification"))

    class Meta:
        verbose_name =_("ATC Class")
        verbose_name_plural=_("ATC Classes")

    def __str__(self):
        return f"{self.code} - {self.name}"

# ============
# 2. Core Product definitions
# These models define what the product is and its sellable unit .
# ============

class Product(models.Model):
    """ The commercial or brand name of a Pharmaceutical product (the parent entity """
    brand_name=models.CharField(max_length=255, unique=True, verbose_name=_("Brand Name"))

    #Protect prevent deleting a manufacturer if any products are linked to it .
    manufacturer =models.ForeignKey(Manufacturer, on_delete=models.PROTECT, verbose_name=_("Manufacturer"))
    atc_class = models.ForeignKey(ATCClass, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("ATC Class"))
    description = models.TextField(blank=True, verbose_name=_("Descriptions"))

    # This is M:M field links to ActiveIngredient vai the Product Ingredient Table
    active_ingredients = models.ManyToManyField(
        ActiveIngredient,
        through='ProductIngredient',
        verbose_name=_("Active Ingredients")
    )
    class Meta:
        verbose_name = _("Product (Brand)")
        verbose_name_plural = _("Product (Brands)")
    def __str__(self):
        return self.brand_name

class ProductIngredient(models.Model):
    """
    Join Table M:M. Stores the strength of a specific ingredient within a Product .
    Needed because one product can have many Ingredients , and we need the strength value.
    """
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient =models.ForeignKey(ActiveIngredient, on_delete=models.CASCADE)
    strength= models.CharField(max_length=50, verbose_name=_("Strength"))

    class Meta:
        #Prevent Redundant data : a product can't list the same ingredients twice.
        unique_together =('product','ingredient')
        verbose_name= _("Product Ingredient")
        verbose_name_plural=_("Product Ingredients")