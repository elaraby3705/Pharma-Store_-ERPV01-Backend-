from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Define choices outside the class for correct Python scoping
COMPANY_TYPES = (
    ('pharmacy', _('Pharmacy')),
    ('supplier', _('Supplier'))
)


# ========================
# 1. COMMERCIAL STRUCTURE (COMPANY & BRANCH)
# ============================

class Company(models.Model):
    """The general organizational entity (Supplier or Pharmacy)."""
    type = models.CharField(max_length=50, choices=COMPANY_TYPES, verbose_name=_("Company Type"))
    name = models.CharField(max_length=255, verbose_name=_("Trade Name"))
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owned_companies', verbose_name=_("Owner"))
    license_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=_("License Number"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Company/Supplier")
        verbose_name_plural = _("Companies and Suppliers")

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class Branch(models.Model):
    """Physical location for Pharmacies (fulfillment center)."""
    # Using string reference for external app dependency
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='branches',
        limit_choices_to={'type': 'pharmacy'},
        verbose_name=_("Parent Company")
    )
    name = models.CharField(max_length=255, verbose_name=_("Branch Name"))
    # FK to Address model from the 'users' app
    # address = models.ForeignKey('users.Address', on_delete=models.PROTECT, verbose_name=_("Location Address"))
    shipping_available = models.BooleanField(default=True, verbose_name=_("Shipping Available"))

    class Meta:
        verbose_name = _("Branch")
        verbose_name_plural = _("Branches")

    def __str__(self):
        return f"{self.company.name} - {self.name}"


# =====================
# 2. INVENTORY & AUDIT
# =====================

class InventoryBatch(models.Model):
    """Stock tracked at the batch/lot level (for unique expiry dates and prices)."""
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='inventory_batches',
                               verbose_name=_("Branch"))
    # FK to ProductVariant from the 'catalog' app (the sellable item)
    # variant = models.ForeignKey('catalog.ProductVariant', on_delete=models.PROTECT, related_name='batches', verbose_name=_("Product Variant"))
    supplier = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'type': 'supplier'},
        verbose_name=_("Supplier")
    )

    expiry_date = models.DateField(null=True, blank=True, verbose_name=_("Expiry Date"))
    qty_on_hand = models.IntegerField(default=0, verbose_name=_("Quantity On Hand"))
    qty_reserved = models.IntegerField(default=0, verbose_name=_("Quantity Reserved"))

    cost_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Cost Price"))
    sale_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Sale Price"))

    is_available = models.BooleanField(default=True, verbose_name=_("Is Available for Sale"))

    class Meta:
        verbose_name = _("Inventory Batch")
        verbose_name_plural = _("Inventory Batches")
        constraints = [
            models.CheckConstraint(check=models.Q(qty_on_hand__gte=0), name='inventory_qty_on_hand_gte_zero'),
            models.CheckConstraint(check=models.Q(qty_reserved__gte=0), name='inventory_qty_reserved_gte_zero'),
        ]


class InventoryMovement(models.Model):
    """Audit log for all changes in stock quantity (Source for Factor XI Data Stream)."""
    MOVEMENT_TYPES = (
        ('purchase', _('Purchase In')),
        ('sale', _('Sale Out')),
        ('adjustment', _('Adjustment')),
    )

    batch = models.ForeignKey(InventoryBatch, on_delete=models.PROTECT, verbose_name=_("Affected Batch"))
    type = models.CharField(max_length=50, choices=MOVEMENT_TYPES, verbose_name=_("Movement Type"))
    delta_qty = models.IntegerField(verbose_name=_("Quantity Change (+/-)"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Movement Time"))
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_("Moved By"))

    class Meta:
        verbose_name = _("Inventory Movement")
        verbose_name_plural = _("Inventory Movements")
        ordering = ['-created_at']


# =====================
# 3. AI READINESS (PREDICTION)
# ===============

class Prediction(models.Model):
    """Stores AI model outputs for demand forecasting."""
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name=_("Branch"))
    # FK to ProductVariant from the 'catalog' app
    # variant = models.ForeignKey('catalog.ProductVariant', on_delete=models.CASCADE, verbose_name=_("Product Variant"))

    horizon_days = models.IntegerField(verbose_name=_("Prediction Horizon (Days)"))
    predicted_demand = models.IntegerField(verbose_name=_("Predicted Demand"))
    model_version = models.CharField(max_length=50, verbose_name=_("Model Version"))
    generated_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Generated At"))

    class Meta:
        verbose_name = _("Demand Prediction")
        verbose_name_plural = _("Demand Predictions")
        # Note: 'variant' is commented out but needed for unique_together constraint
        unique_together = ('branch', 'horizon_days')