from rest_framework import viewsets, permissions, filters
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.pagination import PageNumberPagination

class ReviewPagination(PageNumberPagination):
    page_size = 5

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = ReviewPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['review_text', 'product__name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
