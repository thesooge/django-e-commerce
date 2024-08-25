from django.db import models
from django.utils.translation import gettext as _
from products.models import Product
# Create your models here.


class Order(models.Model):
    first_name = models.CharField(_('firstname'), max_length=100)
    last_name = models.CharField(_('lastname'), max_length=100)
    address = models.CharField(_('address'), max_length=200)
    phone_number = models.CharField(_('phone'), max_length=20)
    description = models.CharField(_('description'), max_length=1000, blank=True)
    is_paid = models.BooleanField(_('ispaid'), default=False)

    order_date = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_('order'), related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_('quantity'), default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.title}'