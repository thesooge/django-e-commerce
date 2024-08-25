from django.db import models
from django.utils.translation import gettext as _
from products.models import Product
from django.contrib.auth import get_user_model
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('User'), null=True)


    first_name = models.CharField(_('FirstName'), max_length=100)
    last_name = models.CharField(_('LastName'), max_length=100)
    address = models.CharField(_('Address'), max_length=200)
    phone_number = models.CharField(_('Phone'), max_length=20)
    description = models.CharField(_('Description'), max_length=1000, blank=True)
    is_paid = models.BooleanField(_('IsPaid?'), default=False)

    order_date = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_('Order'), related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_('Product'), related_name='product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_('Quantity'), default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.title}'