from django.db.models import Sum
from apps.billing.models import Invoice
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def sales_report(request):
    return Response(
        Invoice.objects.aggregate(
            total_sales=Sum('total_amount'),
            total_tax=Sum('tax_amount')
        )
    )
