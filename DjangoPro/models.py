from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    content = models.TextField()
    authorage  = models.IntegerField()
    def __str__(self):
        return self.title