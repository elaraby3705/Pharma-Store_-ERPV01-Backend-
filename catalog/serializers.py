from rest_framework import serializers
from .models import (
    Manufacturer, DosageForm, ActiveIngredient, ATCClass,
    Product, ProductVariant, ProductIngredient
)

# ======
# 1. Lookup serializer (simple Read-only)
# =====

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Manufacturer
        fields = ['id', 'name', 'is_active']
        read_only_fields=['id']

class DosageFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveIngredient
        fields= ['id', 'name']
        read_only_fields= ['id ']


class ActiveIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model= ActiveIngredient
        fields= ['id','name']
        read_only_fields= ['id']
