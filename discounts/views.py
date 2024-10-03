from rest_framework import viewsets
from .models import Discount
from .serializers import DiscountSerializer
from rest_framework.permissions import IsAuthenticated

# ViewSet for managing Discount model
# Provides default CRUD operations for discounts and requires user authentication
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()  # Fetches all Discount objects
    serializer_class = DiscountSerializer  # Uses DiscountSerializer for serialization
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    # Overriding the create method to associate the discount with the logged-in user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Saves the discount with the requesting user
