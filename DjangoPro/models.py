from django.db import models
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    content = models.TextField()
    authorage  = models.IntegerField()
    slug =models.SlugField(unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.title
    
