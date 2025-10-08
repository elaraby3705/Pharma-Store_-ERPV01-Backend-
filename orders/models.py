from django.db import models
from django.utils.translation import gettext_lazy as _
# Assuming these models are imported from their respective apps:
from django.contrib.auth.models import User


# from users.models import Address
# from catalog.models import ProductVariant
# from inventory.models import Branch, InventoryBatch, Company as DeliveryPartner

# ==============================================================================
# 1. SHOPPING CART LOGIC
#    Temporary storage for customer selection before checkout.
# ==============================================================================

class Cart(models.Model):
    """Shopping Cart container for a user."""
    # ERROR FIX 1: Uncommenting customer FK is necessary if you uncomment unique_together on OrderItem, but
    # we leave it commented for now to avoid the circular dependency unless necessary.
    # customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', verbose_name=_("Customer"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated"))

    class Meta:
        verbose_name = _("Shopping Cart")
        verbose_name_plural = _("Shopping Carts")

    def __str__(self):
        # Placeholder str for now, as customer is commented out
        return f"Cart for {self.id}"


class CartItem(models.Model):
    """Specific product variants and quantities within a Cart."""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name=_("Cart"))

    # --- ERROR FIX 2: UNCOMMENTED variant FK to satisfy unique_together constraint ---
    variant = models.ForeignKey('catalog.ProductVariant', on_delete=models.CASCADE, verbose_name=_("Product Variant"))
    # ----------------------------------------------------------------------------------

    quantity = models.IntegerField(default=1, verbose_name=_("Quantity"))
    unit_price_snapshot = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Unit Price Snapshot"))

    class Meta:
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")
        # This constraint now correctly references the 'variant' field above
        unique_together = ('cart', 'variant')

    # =======================


# 2. ORDER CORE AND ITEMS (TRANSACTIONS)
#    The final record of a completed transaction.
# ======================

class Order(models.Model):
    """The committed transaction entity."""
    STATUS_CHOICES = [
        ('pending', _('Pending')), ('confirmed', _('Confirmed')),
        ('packed', _('Packed')), ('shipped', _('Shipped')),
        ('delivered', _('Delivered')), ('cancelled', _('Cancelled'))
    ]
    PAYMENT_CHOICES = [
        ('unpaid', _('Unpaid')), ('paid', _('Paid')),
        ('refunded', _('Refunded'))
    ]

    # ERROR FIX 3: Uncommented critical FKs needed for logic flow (optional, but good practice now)
    customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders', verbose_name=_("Customer"))
    branch = models.ForeignKey('inventory.Branch', on_delete=models.PROTECT, related_name='fulfilled_orders',
                               verbose_name=_("Fulfilling Branch"))
    shipping_address = models.ForeignKey('users.Address', on_delete=models.PROTECT, verbose_name=_("Shipping Address"))
    # ----------------------------------------------------------------------------------------------

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending', verbose_name=_("Order Status"))
    payment_status = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='unpaid',
                                      verbose_name=_("Payment Status"))

    total = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Total Amount"))
    shipping_fee = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name=_("Shipping Fee"))

    placed_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Placed"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ['-placed_at']


class OrderItem(models.Model):
    """Details of products within a specific Order."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_("Order"))

    # --- ERROR FIX 4: UNCOMMENTED variant FK to satisfy unique_together constraint ---
    variant = models.ForeignKey('catalog.ProductVariant', on_delete=models.PROTECT, verbose_name=_("Product Variant"))

    # --- ERROR FIX 5: UNCOMMENTED batch FK required for fulfillment logic ---
    batch = models.ForeignKey('inventory.InventoryBatch', on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name=_("Assigned Batch"))
    # ------------------------------------------------------------------------

    quantity = models.IntegerField(verbose_name=_("Quantity Ordered"))
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Agreed Unit Price"))

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
        # This constraint now correctly references the 'variant' field above
        unique_together = ('order', 'variant')


# ===========
# 3. LOGISTICS AND USER EXPERIENCE
# ===========

class Shipment(models.Model):
    """Tracks the shipment and links it to a delivery partner."""
    SHIPMENT_STATUS = [
        ('ready', _('Ready for Pickup')), ('in_transit', _('In Transit')),
        ('delivered', _('Delivered')), ('failed', _('Failed Delivery'))
    ]

    # 1:1 relationship with the Order
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipment', verbose_name=_("Order"))
    # partner = models.ForeignKey('inventory.Company', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Delivery Partner"))

    tracking_number = models.CharField(max_length=100, unique=True, null=True, blank=True,
                                       verbose_name=_("Tracking Number"))
    status = models.CharField(max_length=50, choices=SHIPMENT_STATUS, default='ready',
                              verbose_name=_("Shipment Status"))
    delivered_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Delivery Date"))

    class Meta:
        verbose_name = _("Shipment")
        verbose_name_plural = _("Shipments")


class Review(models.Model):
    """Customer feedback on a product or service."""
    # customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Customer"))
    # variant = models.ForeignKey('catalog.ProductVariant', on_delete=models.CASCADE, verbose_name=_("Product Variant"))

    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name=_("Rating (1-5)"))
    comment = models.TextField(verbose_name=_("Comment"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        ordering = ['-created_at']