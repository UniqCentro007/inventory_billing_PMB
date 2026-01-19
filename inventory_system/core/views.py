from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .models import Invoice, StockMovement, Return

def dashboard(request):
    # 1. Monthly Sales
    monthly_sales = Invoice.objects.annotate(
        month=TruncMonth('invoice_date')
    ).values('month').annotate(
        total_sales=Sum('total_amount')
    ).order_by('month')

    # 2. Vendor Purchases
    vendor_purchases = StockMovement.objects.filter(
        movement_type='IN'
    ).values('vendor__name').annotate(
        total_quantity=Sum('quantity')
    )

    # 3. Total Tax Collected
    tax_collected = Invoice.objects.aggregate(total_tax=Sum('total_tax'))

    # 4. Return Summary
    return_summary = Return.objects.aggregate(total_returns=Sum('return_amount'))

    context = {
        'monthly_sales': monthly_sales,
        'vendor_purchases': vendor_purchases,
        'tax_collected': tax_collected,
        'return_summary': return_summary,
    }

    return render(request, 'dashboard.html', context)
