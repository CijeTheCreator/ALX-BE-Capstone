from rest_framework import viewsets
from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class WishlistPagination(PageNumberPagination):
    page_size = 5

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = WishlistPagination    

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
