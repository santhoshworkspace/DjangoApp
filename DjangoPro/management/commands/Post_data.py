from DjangoPro.models import Post,Category
from django.core.management.base import BaseCommand
import random
class Command(BaseCommand):
    help = "Started"    
    def handle(self, *args, **options):
        Post.objects.all().delete()
        authors =['Santhosh','viswa']

        titles =['Automic Habits','The intelligent investor']      

        contents =['First post content','First post content']
        
        authorages = 20 , 21

        categories = Category.objects.all()
        for author,title,content,authorage in zip(authors,titles,contents,authorages):
         category = random.choice(categories)
         Post.objects.create(author=author,title=title,content=content,authorage=authorage,category=category)
        self.stdout.write(self.style.SUCCESS("Completed")) 