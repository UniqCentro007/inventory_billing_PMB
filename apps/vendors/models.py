from django.db import models

class Vendor(models.Model):
    VENDOR_TYPE_CHOICES = (
        ('supplier', 'Supplier'),
        ('customer', 'Customer'),
    )

    name = models.CharField(max_length=200)
    vendor_type = models.CharField(
        max_length=20,
        choices=VENDOR_TYPE_CHOICES
    )
    gst_number = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
