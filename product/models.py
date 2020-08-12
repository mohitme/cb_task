from django.db import models
from django.conf import settings
import os
file_path = os.path.join(settings.BASE_DIR, 'product/images')

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    quantity = models.IntegerField(blank=False, default=0)
    img = models.FilePathField(path=file_path)