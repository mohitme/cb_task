from django.db import models
from django.conf import settings
import os
file_path = os.path.join(settings.BASE_DIR, 'product/images')

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    quantity = models.IntegerField(blank=False, default=0)
    img = models.FilePathField(path=file_path)

class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    email = models.EmailField(max_length=150, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=20, blank=False, unique=True)