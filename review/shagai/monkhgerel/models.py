from django.db import models

# Create your models here.

class Todo(models.Model):
    Todo = models.CharField(max_length=255)