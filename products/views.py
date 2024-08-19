from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.urls import reverse_lazy
from .forms import  CommentForm
from .models import Product, ProductComment
from cart.forms import AddToCartForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
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

        messages.success(self.request, _('comment added succsesfully'))


        return super().form_valid(form)


@login_required
def delete_own_comment(request, pk):
    comment = get_object_or_404(ProductComment, pk=pk)
    if comment.author == request.user:
        comment.delete()

    return redirect("product-detail", comment.product.id)




