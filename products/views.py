from rest_framework import viewsets, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class ProductPagination(PageNumberPagination):
    page_size = 2


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ProductPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    filterset_fields = {
        'category__name': ['exact'],         # Filter by category name
        'price': ['gte', 'lte'],             # Filter by price range (greater than, less than)
        'stock_quantity': ['gte']            # Filter by stock availability (in stock)
    }
    search_fields = ['name', 'description', 'category__name']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
