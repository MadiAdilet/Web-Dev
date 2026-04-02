"""
Custom management command to seed the database with
4 categories and 20 products.

Usage:
    python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from api.models import Category, Product


SEED_DATA = {
    'Electronics': [
        ('Smartphone Pro 15', 'Latest flagship smartphone with 6.7" OLED display', 999.99, 50),
        ('Wireless Earbuds X', 'Active noise cancellation, 30h battery', 149.99, 120),
        ('4K Smart TV 55"', 'Ultra HD display with built-in streaming apps', 649.99, 30),
        ('Laptop UltraBook', '14" display, 16GB RAM, 512GB SSD', 1199.99, 25),
        ('Mechanical Keyboard', 'RGB backlit, tactile switches, USB-C', 89.99, 80),
    ],
    'Clothing': [
        ('Classic White T-Shirt', '100% cotton, available in all sizes', 19.99, 200),
        ('Slim Fit Jeans', 'Stretch denim, modern cut', 49.99, 150),
        ('Hooded Sweatshirt', 'Fleece lined, kangaroo pocket', 39.99, 100),
        ('Running Jacket', 'Lightweight, water-resistant, reflective strips', 79.99, 60),
        ('Leather Belt', 'Genuine leather, silver buckle', 24.99, 90),
    ],
    'Books': [
        ('Clean Code', 'A handbook of agile software craftsmanship by Robert C. Martin', 34.99, 75),
        ('The Pragmatic Programmer', '20th Anniversary Edition, your journey to mastery', 44.99, 60),
        ('Design Patterns', 'Elements of reusable object-oriented software', 39.99, 45),
        ('Python Crash Course', 'A hands-on, project-based introduction to programming', 29.99, 110),
        ('Django for Beginners', 'Build websites with Python & Django', 27.99, 85),
    ],
    'Home & Garden': [
        ('Coffee Maker Deluxe', '12-cup programmable, built-in grinder', 89.99, 40),
        ('Yoga Mat Premium', 'Non-slip, eco-friendly, 6mm thick', 34.99, 95),
        ('Indoor Plant Pot Set', 'Set of 3 ceramic pots with drainage', 24.99, 130),
        ('Smart LED Bulb', 'Wi-Fi enabled, 16M colors, voice control', 14.99, 200),
        ('Stainless Steel Water Bottle', '1L, vacuum insulated, keeps cold 24h', 29.99, 170),
    ],
}


class Command(BaseCommand):
    help = 'Seed the database with 4 categories and 20 products'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        created_categories = 0
        created_products = 0

        for category_name, products in SEED_DATA.items():
            category, cat_created = Category.objects.get_or_create(
                name=category_name,
                defaults={'description': f'Everything related to {category_name.lower()}'}
            )
            if cat_created:
                created_categories += 1
                self.stdout.write(f'  ✓ Category created: {category_name}')
            else:
                self.stdout.write(f'  – Category already exists: {category_name}')

            for name, description, price, stock in products:
                product, prod_created = Product.objects.get_or_create(
                    name=name,
                    defaults={
                        'category': category,
                        'description': description,
                        'price': price,
                        'stock': stock,
                    }
                )
                if prod_created:
                    created_products += 1

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! Created {created_categories} categories and {created_products} products.'
        ))
