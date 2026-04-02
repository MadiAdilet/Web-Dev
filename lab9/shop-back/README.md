# Online Shop — Lab 9: Django REST Framework

## Project Structure

```
shop-back/
├── manage.py
├── requirements.txt
├── OnlineShopAPI.postman_collection.json
├── shop_back/
│   ├── __init__.py
│   ├── settings.py          ← rest_framework in INSTALLED_APPS
│   ├── urls.py              ← includes api/ urls
│   └── wsgi.py
└── api/
    ├── __init__.py
    ├── models.py            ← Category, Product
    ├── serializers.py       ← CategorySerializer, ProductSerializer
    ├── views.py             ← CategoryViewSet, ProductViewSet
    ├── urls.py              ← DefaultRouter
    ├── admin.py             ← Category & Product registered
    └── management/
        └── commands/
            └── seed_data.py ← seeds 4 categories + 20 products
```

---

## Setup Instructions

### 1. Create & Activate Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
# Follow prompts: username, email, password
```

### 5. Seed Database (4 categories + 20 products)

```bash
python manage.py seed_data
```

### 6. Run Development Server

```bash
python manage.py runserver
```

---

## API Endpoints

Base URL: `http://127.0.0.1:8000`

### Categories

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/categories/` | List all categories |
| POST | `/api/categories/` | Create a category |
| GET | `/api/categories/<id>/` | Retrieve a category |
| PUT | `/api/categories/<id>/` | Update a category |
| DELETE | `/api/categories/<id>/` | Delete a category |
| GET | `/api/categories/<id>/products/` | List products in a category |

### Products

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/products/` | List all products |
| POST | `/api/products/` | Create a product |
| GET | `/api/products/<id>/` | Retrieve a product |
| PUT | `/api/products/<id>/` | Update a product |
| DELETE | `/api/products/<id>/` | Delete a product |

---

## Sample JSON Payloads (for POST / PUT)

### Create Category
```json
{
  "name": "Sports",
  "description": "Sports equipment and accessories"
}
```

### Create Product
```json
{
  "category": 1,
  "name": "Wireless Mouse",
  "description": "Ergonomic wireless mouse with long battery life",
  "price": 29.99,
  "stock": 75
}
```

---

## Admin Panel

Visit `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

---

## Postman Collection

Import `OnlineShopAPI.postman_collection.json` into Postman.  
The collection contains **11 requests** — 6 for Categories and 5 for Products.  
All POST / PUT requests use **Body → raw → JSON** format.
