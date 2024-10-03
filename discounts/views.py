import logging
from rest_framework import viewsets
from .models import Discount
from .serializers import DiscountSerializer
from rest_framework.permissions import IsAuthenticated


logger = logging.getLogger(__name__)


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print("Hello World")
        print(self.request)
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        print(request.user)
        return super().list(request, *args, **kwargs)

