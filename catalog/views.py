from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Manufacturer, DosageForm, ActiveIngredient, ATCClass, Product,
    ProductVariant
)
from .serializers import (
    ManufacturerSerializer, DosageFormSerializer, ActiveIngredientSerializer,
    ATCClassSerializer, ProductVariantSerializer, ProductSerializer
)

from django.db import transaction
# # Used in ProductSerializer's overridden methods

# -------------
# Lookup Table ViewSets (CRUD - Admin Access Required)
# -------------

class ManufacturerViewSet(viewsets.ModelViewSet):
    """CRUD for Manufacturer. Admin only."""
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [permissions.IsAdminUser]

class DosageFormVIewSet(viewsets.ModelViewSet):
    """CRUD for DosageForm. admin only"""
    queryset = DosageForm.objects.all()
    serializer_class = DosageFormSerializer
    permission_classes = [permissions.IsAdminUser]

class ActiveIngredientViewSet(viewsets.ModelViewSet):
    """CRUD for ActiveIngredient. Admin only."""
    queryset = ActiveIngredient.objects.all()
    serializer_class = ActiveIngredientSerializer
    permission_classes = [permissions.IsAdminUser]

class ATCClassViewSet(viewsets.ModelViewSet):
    """CRUD for ATCClass. Admin only."""
    queryset = ATCClass.objects.all()
    serializer_class = ATCClassSerializer
    permission_classes = [permissions.IsAdminUser]

# --------------
# Product ViewSet (Issue #4: Admin CRUD for Parent Product)
# -------------


