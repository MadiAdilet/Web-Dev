from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet

# DefaultRouter automatically generates URL patterns for all standard actions:
#   GET    /api/categories/          → list
#   POST   /api/categories/          → create
#   GET    /api/categories/<pk>/     → retrieve
#   PUT    /api/categories/<pk>/     → update
#   PATCH  /api/categories/<pk>/     → partial_update
#   DELETE /api/categories/<pk>/     → destroy
#   GET    /api/categories/<pk>/products/ → custom action
# (same for products, without the custom action)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
