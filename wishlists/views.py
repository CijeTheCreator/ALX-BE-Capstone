from rest_framework import viewsets
from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Custom pagination class for WishlistViewSet
# Limits the number of wishlists per page to 2
class WishlistPagination(PageNumberPagination):
    page_size = 2


# ViewSet for managing Wishlist model
# Provides CRUD operations for wishlist, with authentication and filtering options
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = WishlistPagination    

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
