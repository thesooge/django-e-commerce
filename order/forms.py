from django import forms
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'description']
        
        widegts = {'address':forms.Textarea(attrs={'rows':2}),
                'description' : forms.Textarea(attrs={'rows':2})
                }
    