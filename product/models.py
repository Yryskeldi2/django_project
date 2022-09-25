from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    desc = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)