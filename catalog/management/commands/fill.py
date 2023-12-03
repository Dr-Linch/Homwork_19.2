from django.core.management import BaseCommand
from django.db import connection
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

        categoryes_list = [
            {'category_name': 'Office', 'category_description': 'Just office products'},
            {'category_name': 'Chemicals', 'category_description': 'Just house chemical'},
            {'category_name': 'Vegetable', 'category_description': 'Natural vegetables'},
            {'category_name': 'Fruits', 'category_description': 'Fresh fruits'},
            {'category_name': 'Meat', 'category_description': 'Quality meat'}
        ]

        category_for_create = []
        for category_item in categoryes_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)