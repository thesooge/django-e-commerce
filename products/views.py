from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .forms import  CommentForm
from .models import Product, ProductComment
# Create your views here.

class ProductLists(generic.ListView):
    model = Product
    template_name = 'products/product-list.html'
    context_object_name = 'products'

class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = 'product'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = CommentForm()

        return context
    
class ProductComments(generic.CreateView):
    model = ProductComment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        return super().form_valid(form)



