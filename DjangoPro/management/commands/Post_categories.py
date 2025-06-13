from DjangoPro.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="command categories"
    categories =['Habits','investment']

    for categoryname in categories:
        Category.objects.create(name=categoryname)
    def handle(self, *args, **options):
        return 