from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='static/products/')
