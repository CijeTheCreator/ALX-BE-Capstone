from rest_framework import serializers
from .models import Discount

# Serializer for the Discount model, handling the creation and representation of discounts
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'
