from django.shortcuts import render, redirect
from .models import Price, Product
from .forms import PriceForm

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

    # Render the price list template with the form and prices
    return render(request, 'prices/price_list.html', {'form': form, 'prices': prices})
