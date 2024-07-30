from django.shortcuts import render
from django.views import generic


from .models import Product
# Create your views here.

class ProductLists(generic.ListView):
    model = Product
    template_name = 'products/product-list.html'
    context_object_name = 'products'

class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = 'product'    
