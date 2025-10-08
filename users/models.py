from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# =====================
# 1. USER PROFILE AND ROLES
# =====================

class UserProfile(models.Model):
    """An extension profile linked 1:1 to Django's core User."""
    USER_ROLES = (
        ('customer', _('Customer')),
        ('pharmacy_owner', _('Pharmacy Owner')),
        ('supplier_owner', _('Supplier Owner')),
        ('staff', _('Staff')),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name=_("User Account")
    )
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    phone = models.CharField(max_length=20, unique=True, verbose_name=_("Phone Number"))
    role = models.CharField(max_length=50, choices=USER_ROLES, default='customer', verbose_name=_("Role"))
    default_language = models.CharField(
        max_length=10,
        default='en',
        choices=[('ar', 'العربية'), ('en', 'English')],
        verbose_name=_("Default Language")
    )

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")

    def __str__(self):
        return self.full_name or self.user.username


# ===========================
# 2. ADDRESS (REUSABLE ENTITY)
# ===========================

class Address(models.Model):
    """Reusable address model for shipping and branch location."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='addresses',
        verbose_name=_("Address Owner")
    )
    governorate = models.CharField(max_length=100, verbose_name=_("Governorate"))
    city = models.CharField(max_length=100, verbose_name=_("City"))
    district = models.CharField(max_length=100, verbose_name=_("District"))
    street = models.CharField(max_length=255, verbose_name=_("Street"))
    building_no = models.CharField(max_length=50, verbose_name=_("Building Number"))
    apartment = models.CharField(max_length=50, blank=True, verbose_name=_("Apartment Number"))

    geo_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name=_("Latitude"))
    geo_lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name=_("Longitude"))

    is_default = models.BooleanField(default=False, verbose_name=_("Default Address"))

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
        unique_together = ('user', 'is_default')

    def __str__(self):
        return f"{self.city}, {self.street}"