from django.db import models
from django.utils.translation import gettext_lazy as _


# ===============================
# 1. LOOKUP TABLES (STATIC DICTIONARIES)
# ================================

class Manufacturer(models.Model):
    """The core entity for the pharmaceutical company that produces the drug."""
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Manufacturer Name"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Manufacturer")
        verbose_name_plural = _("Manufacturers")

    def __str__(self):
        return self.name


class DosageForm(models.Model):
    """The physical form of the medicine (e.g., Tablet, Syrup, Capsule)."""
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Dosage Form"))

    class Meta:
        verbose_name = _("Dosage Form")
        verbose_name_plural = _("Dosage Forms")

    def __str__(self):
        return self.name


class ActiveIngredient(models.Model):
    """The chemical component responsible for the therapeutic effect (e.g., Paracetamol)."""
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Active Ingredient"))

    class Meta:
        verbose_name = _("Active Ingredient")
        verbose_name_plural = _("Active Ingredients")

    def __str__(self):
        return self.name


class ATCClass(models.Model):
    """WHO's Anatomical Therapeutic Chemical (ATC) classification system (optional)."""
    code = models.CharField(max_length=10, unique=True, verbose_name=_("ATC Code"))
    name = models.CharField(max_length=255, verbose_name=_("ATC Classification"))

    class Meta:
        verbose_name = _("ATC Class")
        verbose_name_plural = _("ATC Classes")

    def __str__(self):
        return f"{self.code} - {self.name}"


# ==========================
# 2. CORE PRODUCT DEFINITIONS
# ==========================

class Product(models.Model):
    """The commercial or brand name of a pharmaceutical product (the PARENT entity)."""
    brand_name = models.CharField(max_length=255, unique=True, verbose_name=_("Brand Name"))

    # PROTECT prevents deleting a manufacturer if any products are linked to it.
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, verbose_name=_("Manufacturer"))
    atc_class = models.ForeignKey(ATCClass, on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name=_("ATC Class"))
    description = models.TextField(blank=True, verbose_name=_("Description"))

    # M:M Relationship defined via the ProductIngredient table
    active_ingredients = models.ManyToManyField(
        ActiveIngredient,
        through='ProductIngredient',
        verbose_name=_("Active Ingredients")
    )

    class Meta:
        verbose_name = _("Product (Brand)")
        verbose_name_plural = _("Products (Brands)")

    def __str__(self):
        return self.brand_name


class ProductIngredient(models.Model):
    """Intermediate table to store the strength of an ingredient in a Product (M:M)."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(ActiveIngredient, on_delete=models.CASCADE)
    strength = models.CharField(max_length=50, verbose_name=_("Strength"))

    class Meta:
        # Prevents redundant data: a product can't list the same ingredient twice.
        unique_together = ('product', 'ingredient')
        verbose_name = _("Product Ingredient")
        verbose_name_plural = _("Product Ingredients")


class ProductVariant(models.Model):
    """THE SELLABLE UNIT. This is the specific item linked to Inventory and Orders."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Parent Product"))

    # Using string reference for safety, though DosageForm is defined above
    dosage_form = models.ForeignKey('DosageForm', on_delete=models.PROTECT, verbose_name=_("Dosage Form"))

    strength_text = models.CharField(
        max_length=100,
        help_text=_("e.g., 500 mg, 10 mg/5ml"),
        verbose_name=_("Strength Text")
    )
    pack_size = models.IntegerField(verbose_name=_("Pack Size (Units)"))
    barcode_gtin = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_("Barcode/GTIN"))
    is_prescription_only = models.BooleanField(default=False, verbose_name=_("Prescription Only (Rx)"))
    is_otc = models.BooleanField(default=False, verbose_name=_("Over-The-Counter (OTC)"))

    class Meta:
        # Ensures no two variants have the exact same specification
        unique_together = ('product', 'dosage_form', 'pack_size')
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Product Variants")

    def __str__(self):
        return f"{self.product.brand_name} - {self.strength_text} ({self.dosage_form.name})"