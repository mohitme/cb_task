from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    quantity = models.IntegerField(blank=False, default=0)
    img = models.FilePathField(path='/product/images')