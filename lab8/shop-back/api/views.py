import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Product, Category


def product_to_dict(product):
    return {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active,
        'category': {
            'id': product.category.id,
            'name': product.category.name,
        }
    }


def category_to_dict(category):
    return {
        'id': category.id,
        'name': category.name,
    }


@require_GET
def product_list(request):
    """GET /api/products/ — List of all Products"""
    products = Product.objects.select_related('category').all()
    data = [product_to_dict(p) for p in products]
    return JsonResponse(data, safe=False)


@require_GET
def product_detail(request, id):
    """GET /api/products/<id>/ — Get one Product by ID"""
    try:
        product = Product.objects.select_related('category').get(id=id)
        return JsonResponse(product_to_dict(product))
    except Product.DoesNotExist:
        return JsonResponse({'error': f'Product with id={id} not found'}, status=404)


@require_GET
def category_list(request):
    """GET /api/categories/ — List of all Categories"""
    categories = Category.objects.all()
    data = [category_to_dict(c) for c in categories]
    return JsonResponse(data, safe=False)


@require_GET
def category_detail(request, id):
    """GET /api/categories/<id>/ — Get one Category by ID"""
    try:
        category = Category.objects.get(id=id)
        return JsonResponse(category_to_dict(category))
    except Category.DoesNotExist:
        return JsonResponse({'error': f'Category with id={id} not found'}, status=404)


@require_GET
def category_products(request, id):
    """GET /api/categories/<id>/products/ — List of Products by Category"""
    try:
        category = Category.objects.get(id=id)
        products = Product.objects.select_related('category').filter(category=category)
        data = [product_to_dict(p) for p in products]
        return JsonResponse(data, safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': f'Category with id={id} not found'}, status=404)
