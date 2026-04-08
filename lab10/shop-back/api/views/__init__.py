# ─────────────────────────────────────────────────────────────────────────────
# Switch between view levels by changing the import below.
# All levels expose the same interface.
#
# Level 2 (FBV):     from api.views.fbv      import ...
# Level 3 (CBV):     from api.views.cbv      import ...
# Level 4 (Mixins):  from api.views.mixins   import ...
# Level 5 (Generic): from api.views.generics import ...  ← ACTIVE
# ─────────────────────────────────────────────────────────────────────────────

from api.views.generics import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryProductsAPIView,
)
