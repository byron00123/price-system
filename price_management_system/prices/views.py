from django.db.models import Count
from django.shortcuts import render, redirect
from .models import Price, Product
from .forms import PriceForm
import json

def price_list(request):
    # Retrieve existing products from the database
    products = Product.objects.all()

    # Check if the form is submitted
    if request.method == 'POST':
        # Create a PriceForm instance with the submitted data
        form = PriceForm(request.POST, product_choices=products)
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to the price list page to prevent form resubmission on refresh
            return redirect('price_list')
    else:
        # If the request method is GET, create an empty PriceForm instance
        form = PriceForm(product_choices=products)

    # Retrieve existing prices from the database
    prices = Price.objects.all()

    # Aggregate farmgate prices by date
    farmgate_prices_by_date = Price.objects.values('date').annotate(total_farmgate_price=Count('farmgate_price')).order_by('date')

    # Prepare data for the chart
    dates = [entry['date'].strftime('%Y-%m-%d') for entry in farmgate_prices_by_date]
    farmgate_prices = [entry['total_farmgate_price'] for entry in farmgate_prices_by_date]

    # Pass data to the template
    context = {
        'form': form,
        'prices': prices,
        'dates': json.dumps(dates),
        'farmgate_prices': json.dumps(farmgate_prices),
    }

    # Render the price list template with the form and prices
    return render(request, 'prices/price_list.html', context)