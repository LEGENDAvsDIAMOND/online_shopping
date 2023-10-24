from django.shortcuts import render

from rest_framework import viewsets
from product.models import Product
from product.serializers import ProductSerializer
from django.http import JsonResponse
from django.utils.timezone import now
from product.models import Product
from django.db.models import Count

def best_selling_product(request):
    best_selling = Product.objects.annotate(total_sales=Count('items')).order_by('-total_sales').first()

    if best_selling:
        data = {
            'product_id': best_selling.id,
            'product_name': best_selling.name,
            'total_sales': best_selling.total_sales
        }
    else:
        data = {
            'product_id': None,
            'product_name': None,
            'total_sales': 0
        }

    return JsonResponse(data)

def expired_products(request):
    expired_products = Product.objects.filter(end_date__lt=now())
    data = {'expired_products': list(expired_products.values())}
    return JsonResponse(data)

def total_product_amount(request):
    total_amount = Product.objects.count()
    data = {'total_amount': total_amount}
    return JsonResponse(data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer