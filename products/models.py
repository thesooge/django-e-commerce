from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Product(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    status = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail' ,args=[self.id])