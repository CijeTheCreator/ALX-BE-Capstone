from rest_framework import viewsets, permissions, filters
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.pagination import PageNumberPagination


# Custom pagination class for ReviewViewSet
# Limits the number of reviews per page to 5
class ReviewPagination(PageNumberPagination):
    page_size = 5


# ViewSet for managing Review model
# Provides CRUD operations for reviews, with authentication and filtering options
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = ReviewPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['review_text', 'product__name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
