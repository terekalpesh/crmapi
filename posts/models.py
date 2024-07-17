from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.   
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    summary = models.CharField(max_length=200, blank=False, null=True)
    document = models.FileField(upload_to='media', default='documents/default_file.pdf')
    categories = models.ManyToManyField('Category')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category