from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

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
    
class ProductComment(models.Model):
    choices = (
        ('1' , 'very bad'),
        ('2' , 'bad'),
        ('3' , 'typical'),
        ('4' , 'good'),
        ('5' , 'super')
    )
    
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    stars = models.CharField(max_length=10, choices=choices)



    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product-detail' ,args=[self.product.id])


    
