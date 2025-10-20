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

# ====
#2. Product serializer (complex / Nested Data )
# ===

class ProductIngredientSerializer(serializers.ModelSerializer):
    """Serializer for the M:M relationship, including the 'strength' field."""
    # Display the ingredient's name directly instead of just the ID
    ingredient_name = serializers.CharField(source='ingredient.name', read_only=True)

    class Meta:
        model = ProductIngredient
        fields = ['ingredient_name', 'strength']


