from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty forms to display

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ['last_name', 'is_paid']
    inlines = [OrderItemAdmin]  # Include ProductComment as inline

@admin.register(OrderItem)
class OrderItemMain(admin.ModelAdmin):  # Corrected the class name
    list_display = ['order', 'product', 'quantity']