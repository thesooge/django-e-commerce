
from django.urls import path
from .views import cart_list, add_to_cart, remove_from_cart

app_name = 'cart'

urlpatterns = [
    path('', cart_list, name='cart_detail'),
    path('add/<int:product_id>', add_to_cart, name='addcart'),
    path('remove/<int:product_id>', remove_from_cart, name='removecart'),
]
