from django.contrib import admin

from .models import Product, ProductComment

# Register your models here.
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'status']

# @admin.register(ProductComment)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['product', 'author', 'stars']    

# Inline class for ProductComment
class ProductCommentInline(admin.TabularInline):
    model = ProductComment
    extra = 1  # Number of empty forms to display

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    inlines = [ProductCommentInline]  # Include ProductComment as inline

@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):  # Corrected the class name
    list_display = ['product', 'author', 'stars']