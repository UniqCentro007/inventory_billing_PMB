from django.db import models
from apps.products.models import Product

class StockTransaction(models.Model):
    TRANSACTION_TYPE = (
        ('IN', 'Stock Inward'),
        ('OUT', 'Stock Outward'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.transaction_type == 'IN':
            self.product.stock_quantity += self.quantity
        else:
            if self.product.stock_quantity < self.quantity:
                raise ValueError("Insufficient Stock")
            self.product.stock_quantity -= self.quantity

        self.product.save()
        super().save(*args, **kwargs)
