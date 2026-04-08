"""
Level 2: Function-Based Views (FBV)
Using @api_view decorator from Django REST Framework.

Key differences from raw Django:
- @api_view instead of @csrf_exempt
- request.data instead of json.loads(request.body)
- Response(...) instead of JsonResponse(...)
- status.HTTP_* constants for status codes
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Product
from api.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def products_list(request):
    """
    GET  /api/v2/products/  — list all products
    POST /api/v2/products/  — create new product
    """
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, product_id):
    """
    GET    /api/v2/products/<id>/  — get one product
    PUT    /api/v2/products/<id>/  — update product
    DELETE /api/v2/products/<id>/  — delete product
    """
    try:
        product = Product.objects.select_related('category').get(id=product_id)
    except Product.DoesNotExist:
        return Response(
            {'error': f'Product with id={product_id} not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
