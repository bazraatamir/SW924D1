from django.db import models

# Create your models here.
class BlogModel(models.Model):
    Title= models.CharField(max_length=255)
    article = models.TextField()
    Image= models.CharField(max_length=255)