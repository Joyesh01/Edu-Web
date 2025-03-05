# Create your models here.
from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    comment = models.TextField()