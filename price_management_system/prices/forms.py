from django import forms
from .models import Price

class PriceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        product_choices = kwargs.pop('product_choices', None)
        super(PriceForm, self).__init__(*args, **kwargs)
        if product_choices:
            self.fields['product'].queryset = product_choices

    class Meta:
        model = Price
        fields = ['product', 'farmgate_price', 'retail_price', 'location']
