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

class DosageFormViewSet(viewsets.ModelViewSet):
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
class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD API for product (Brand) entity.
    Handles nested creation /update if ingredients via overridden serializer methods.
    """
    queryset = Product.objects.prefetch_related('active_ingredients').all()
    serializer_class = ProductSerializer
    # Enforce Gherkin : only authentication admins can perform CRUD
    permission_classes = [permissions.IsAdminUser]


# ---------------
# Product Variant ViewSet (Issue #3: Public Read-Only)
# --------------

class ProductVariantViewSet(viewsets.ReadOnlyModelViewSet):
    """Public read-only API for browsing and searching sellable units."""
    queryset = ProductVariant.objects.select_related('product', 'dosage_form').all()
    serializer_class = ProductVariantSerializer

    #Public access : anyone can read the catalog
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #Enable filtering and searching
    filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    #search fields (searching by brand name , ingredient, etc).
    search_fields = ['product__brand_name', 'product__active_ingredients__name','barcode_gtin' ]

    #Filter fields (for advanced sidebar filtering
    filterset_fields =['is_prescription_only', 'is_otc', 'dosage_form']

    #Ordering fields (e.g., sorting by name or pack size)
    ordering_fields= ['product__brand_name', 'pack_size']