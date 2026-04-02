from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing categories.

    Provides: list, create, retrieve, update, partial_update, destroy
    Custom action: products — returns all products for a given category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'], url_path='products')
    def products(self, request, pk=None):
        """
        GET /api/categories/<id>/products/
        Returns all products that belong to the specified category.
        """
        category = self.get_object()
        products = category.products.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing products.

    Provides: list, create, retrieve, update, partial_update, destroy
    """
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
