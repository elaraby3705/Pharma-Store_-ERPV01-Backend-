from django.db import router
from django.urls import  path, include
from rest_framework.routers import  DefaultRouter
from .views import (

ManufacturerViewSet, DosageFormViewSet, ActiveIngredientViewSet,
    ATCClassViewSet, ProductVariantViewSet, ProductViewSet # <-- Includes ProductViewSet
)

# Initialize the router to auto-generate URLS

router =DefaultRouter()

# Register all ViewSets
router.register('manufacturers', ManufacturerViewSet)
router.register('dosages', DosageFormViewSet)
router.register('ingredients', ActiveIngredientViewSet)
router.register('atc-classes', ATCClassViewSet)

#  Registration: /api/v1/products/
router.register('variants', ProductVariantViewSet)

# Registrations: /api/vi/variants/
router.register('products', ProductViewSet)

urlpatterns = [
    # Includes all routes from the router
    path('', include(router.urls)),
]