from django.contrib import admin

from .models import Product, ProductComment

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']

@admin.register(ProductComment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'stars']    
