from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    farmgate_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.product.name} - {self.date}"
