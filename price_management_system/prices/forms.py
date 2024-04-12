from django import forms
from .models import Price

class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['product', 'farmgate_price', 'retail_price', 'date', 'location']
