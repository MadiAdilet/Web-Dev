from django.urls import path

# ─── Level 5: Generics (ACTIVE — main endpoints) ─────────────────────────────
from api.views import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryProductsAPIView,
)

# ─── Level 2: FBV ─────────────────────────────────────────────────────────────
from api.views.fbv import (
    products_list as fbv_products_list,
    product_detail as fbv_product_detail,
)

# ─── Level 3: CBV ─────────────────────────────────────────────────────────────
from api.views.cbv import (
    ProductListAPIView as CBVProductList,
    ProductDetailAPIView as CBVProductDetail,
)

# ─── Level 4: Mixins ──────────────────────────────────────────────────────────
from api.views.mixins import (
    ProductListAPIView as MixinProductList,
    ProductDetailAPIView as MixinProductDetail,
)

urlpatterns = [

    # Level 5 — Generics (основные эндпоинты)
    path('products/',                       ProductListAPIView.as_view(),      name='product-list'),
    path('products/<int:product_id>/',      ProductDetailAPIView.as_view(),    name='product-detail'),
    path('categories/',                     CategoryListAPIView.as_view(),     name='category-list'),
    path('categories/<int:pk>/',            CategoryDetailAPIView.as_view(),   name='category-detail'),
    path('categories/<int:id>/products/',   CategoryProductsAPIView.as_view(), name='category-products'),

    # Level 2 — FBV
    path('v2/products/',                    fbv_products_list,                 name='fbv-product-list'),
    path('v2/products/<int:product_id>/',   fbv_product_detail,                name='fbv-product-detail'),

    # Level 3 — CBV
    path('v3/products/',                    CBVProductList.as_view(),          name='cbv-product-list'),
    path('v3/products/<int:product_id>/',   CBVProductDetail.as_view(),        name='cbv-product-detail'),

    # Level 4 — Mixins
    path('v4/products/',                    MixinProductList.as_view(),        name='mixin-product-list'),
    path('v4/products/<int:product_id>/',   MixinProductDetail.as_view(),      name='mixin-product-detail'),
]
