from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'gst_percentage', 'stock_quantity', 'is_active')
    search_fields = ('name', 'code')
