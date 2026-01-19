from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    
def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    address = models.TextField()

def __str__(self):
        return self.name
    
class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    total_tax = models.DecimalField(max_digits=12, decimal_places=2)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
class Return(models.Model):
    invoice_item = models.ForeignKey('InvoiceItem', on_delete=models.CASCADE)
    return_quantity = models.IntegerField()
    return_amount = models.DecimalField(max_digits=12, decimal_places=2)
    return_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Increase stock when a return is recorded
        product = self.invoice_item.product
        product.stock_quantity += self.return_quantity
        product.save()
        super().save(*args, **kwargs)

class CreditNote(models.Model):
    return_entry = models.OneToOneField(Return, on_delete=models.CASCADE)
    credit_amount = models.DecimalField(max_digits=12, decimal_places=2)
    issued_date = models.DateField(auto_now_add=True)
