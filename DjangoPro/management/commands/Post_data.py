from DjangoPro.models import Post
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Started"    
    def handle(self, *args, **options):
        Post.objects.all().delete()
        authors =['Santhosh','viswa']

        titles =['Automic Habits','The intelligent investor']      

        contents =['First post content','First post content']
        
        authorages = 20 , 21
        for author,title,content,authorage in zip(authors,titles,contents,authorages):
         Post.objects.create(author=author,title=title,content=content,authorage=authorage)
        self.stdout.write(self.style.SUCCESS("Completed")) 