from django.shortcuts import render
from django.http import HttpResponse
from storefront.models import product


def storefront_view(request):
    product_list = product.objects.order_by('product_name')
    product_dict = {'product' : product_list}
    return render(request, 'storefront/index.html', context=product_dict)


def item_detail_view(request, pk):
    item = product.objects.get(pk = pk)
    product_dict = {'product':item}
    return render(request,'storefront/item_detail.html', context = product_dict)