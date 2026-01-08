from django.db import models
from apps.products.models import Product
from apps.vendors.models import Vendor

class Invoice(models.Model):
    customer = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice, related_name='items', on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
