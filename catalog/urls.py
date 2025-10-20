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