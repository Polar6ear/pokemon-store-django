from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'Address_line_1', 'Address_line_2', 'country', 'state', 'city', 'order_note']


