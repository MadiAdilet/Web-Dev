# shop-back

Django REST API backend for the Online Shop (Lab 8).

## Project Structure

```
shop-back/
├── manage.py
├── requirements.txt
├── .gitignore
├── shop_back/          # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── api/                # API application
    ├── __init__.py
    ├── apps.py
    ├── admin.py
    ├── models.py       # Category, Product
    ├── views.py        # API endpoints
    ├── urls.py
    └── migrations/
        └── 0001_initial.py
```

## Setup & Run

```bash
# 1. Create and activate virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. (Optional) Create superuser for admin panel
python manage.py createsuperuser

# 5. Run development server
python manage.py runserver
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products/` | List all products |
| GET | `/api/products/<id>/` | Get product by ID |
| GET | `/api/categories/` | List all categories |
| GET | `/api/categories/<id>/` | Get category by ID |
| GET | `/api/categories/<id>/products/` | List products by category |

## Models

### Category
- `id` — AutoField (PK)
- `name` — CharField

### Product
- `id` — AutoField (PK)
- `name` — CharField
- `price` — FloatField
- `description` — TextField
- `count` — IntegerField
- `is_active` — BooleanField
- `category` — ForeignKey → Category
