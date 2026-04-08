"""
Level 4: Mixins
Using DRF Mixins + GenericAPIView.

Key differences from CBV:
- No manual serializer logic — mixins handle it
- Must set queryset and serializer_class on the class
- Methods just delegate to mixin methods: self.list(), self.create(), etc.
- lookup_url_kwarg tells DRF which URL param to use for object lookup
"""

from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from api.models import Product
from api.serializers import ProductSerializer


class ProductListAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView
):
    """
    GET  /api/v4/products/  — list all (ListModelMixin)
    POST /api/v4/products/  — create   (CreateModelMixin)
    """
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):
    """
    GET    /api/v4/products/<id>/  — retrieve (RetrieveModelMixin)
    PUT    /api/v4/products/<id>/  — update   (UpdateModelMixin)
    DELETE /api/v4/products/<id>/  — destroy  (DestroyModelMixin)
    """
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'  # maps <product_id> from URL to object lookup

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
