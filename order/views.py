from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItem

# Create your views here.

@login_required
def create_order(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request,_('The cart is empy first add product to your cart!'))        
        return redirect('product-list')

    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.save()

        for item in cart:
            product = item['product_obj']
            OrderItem.objects.create(
                order = order,
                product = product,
                quantity = item['quantity'],
                price = product.price,
            )    

        cart.clear()

        request.user.first_name = order.first_name
        request.user.last_name = order.last_name
        request.user.save() 

        request.session['order_id'] = order.id

        return redirect('create_order')  
     


    return render(request, 'order/order.html', {'form':order_form,})