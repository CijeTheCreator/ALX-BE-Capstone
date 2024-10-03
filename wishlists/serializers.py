from rest_framework import serializers
from .models import Wishlist

# Serializer for the Wishlist model, handling the creation and representation of wishlists
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['wishlist_id', 'user', 'product']
