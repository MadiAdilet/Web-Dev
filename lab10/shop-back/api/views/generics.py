"""
Level 5: Generic Views — the most concise approach.
Almost no code — DRF does everything automatically.

ListCreateAPIView       = GET (list) + POST (create)
RetrieveUpdateDestroyAPIView = GET + PUT + DELETE for one object

Also includes Category endpoints and custom CategoryProductsAPIView.
"""

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer


# ─── Product endpoints ────────────────────────────────────────────────────────

class ProductListAPIView(generics.ListCreateAPIView):
    """
    GET  /api/products/  — list all products
    POST /api/products/  — create new product
    """
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/products/<product_id>/  — get one product
    PUT    /api/products/<product_id>/  — update product
    DELETE /api/products/<product_id>/  — delete product
    """
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'


# ─── Category endpoints ───────────────────────────────────────────────────────

class CategoryListAPIView(generics.ListCreateAPIView):
    """
    GET  /api/categories/  — list all categories
    POST /api/categories/  — create new category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/categories/<id>/  — get one category
    PUT    /api/categories/<id>/  — update category
    DELETE /api/categories/<id>/  — delete category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryProductsAPIView(APIView):
    """
    GET /api/categories/<id>/products/  — list products by category
    """

    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response(
                {'error': f'Category with id={id} not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        products = Product.objects.select_related('category').filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
