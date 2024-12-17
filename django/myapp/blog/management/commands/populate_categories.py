from typing import Any
from django.core.management.base import BaseCommand
from blog.models import Category

class Command(BaseCommand):
    help = "This will inserts category data in Database"

    def handle(self, *args, **options):
        # Delete Existing data
        Category.objects.all().delete()

        categories = ['Sports','Tech','Art','Science','Food']


        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Complted Inserting Data!"))

