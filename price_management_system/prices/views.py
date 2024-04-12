from django.shortcuts import render

from .models import Price 
from .forms import PriceForm  # Import your PriceForm

def price_list(request):
    # Assuming you have a PriceForm defined in forms.py
    form = PriceForm()

    # You may have other logic to retrieve the prices from the database
    prices = Price.objects.all()

    return render(request, 'prices/price_list.html', {'form': form, 'prices': prices})
