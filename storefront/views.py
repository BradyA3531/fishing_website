from django.shortcuts import render
from django.http import HttpResponse
from storefront.models import product


def storefront_view(request):
    product_list = product.objects.order_by('product_name')
    product_dict = {'product' : product_list}
    return render(request, 'storefront/index.html', context=product_dict)