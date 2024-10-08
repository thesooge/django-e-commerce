from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from products.models import Product
from .forms import AddToCartForm

# Create your views here.

def cart_list(request):

    cart = Cart(request)

    for item in cart:
        item['product_update_quantity'] = AddToCartForm(initial={'quantity' : item['quantity'], 'inplace' : True })

    return render(request, 'cart/cart-list.html', {'cart' : cart ,})

def add_to_cart(request, product_id):

    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)




    form = AddToCartForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace_current_quantity =  cleaned_data['inplace'])

    return redirect('cart:cart_detail')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

