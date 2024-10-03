from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WishlistViewSet

router = DefaultRouter()
router.register(r'wishlists', WishlistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
