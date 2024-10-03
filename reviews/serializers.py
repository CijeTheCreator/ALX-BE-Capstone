from rest_framework import serializers
from .models import Review

# Serializer for the Review model, handling the creation and representation of reviews
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['review_id', 'rating', 'review_text', 'created_date', 'user', 'product']
