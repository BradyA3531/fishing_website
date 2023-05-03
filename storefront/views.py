from django.shortcuts import render
from django.http import HttpResponse
from storefront.models import product
from account.views import signout
from account.models import Account
from .forms import orderForm
from .models import order
import datetime



def filterByBait(request):
    product_list = product.objects.filter(product_type = 'bait')
    print(product_list)
    if request.user.is_authenticated:
        name = request.user.fname
        product_dict = {'product' : product_list, 'fname': name}
        return render(request, 'storefront/index.html', context=product_dict)
        
    else:
        product_dict = {'product' : product_list}
        return render(request, 'storefront/index.html', context=product_dict)

def filterByMisc(request):
    product_list = product.objects.filter(product_type = 'misc')
    print(product_list)
    if request.user.is_authenticated:
        name = request.user.fname
        product_dict = {'product' : product_list, 'fname': name}
        return render(request, 'storefront/index.html', context=product_dict)
        
    else:
        product_dict = {'product' : product_list}
        return render(request, 'storefront/index.html', context=product_dict)

def filterByLures(request):
    product_list = product.objects.filter(product_type = 'lure')
    if request.user.is_authenticated:
        name = request.user.fname
        product_dict = {'product' : product_list, 'fname': name}
        return render(request, 'storefront/index.html', context=product_dict)
    else:
        product_dict = {'product' : product_list}
        return render(request, 'storefront/index.html', context=product_dict)

def filterByRods(request):
    product_list = product.objects.filter(product_type = 'rod')
    if request.user.is_authenticated:
        name = request.user.fname
        product_dict = {'product' : product_list, 'fname': name}
        return render(request, 'storefront/index.html', context=product_dict)
    else:
        product_dict = {'product' : product_list}
        return render(request, 'storefront/index.html', context=product_dict)

def storefront_view(request):
    product_list = product.objects.order_by('product_name')
    if request.user.is_authenticated:
        name = request.user.fname
        product_dict = {'product' : product_list, 'fname': name}
        return render(request, 'storefront/index.html', context=product_dict)    
    else:
        product_dict = {'product' : product_list}
        return render(request, 'storefront/index.html', context=product_dict)
    


def item_detail_view(request, pk):
    item = product.objects.get(pk = pk)
    product_dict = {'product':item}
    return render(request,'storefront/item_detail.html', context = product_dict)

def buy_page_view(request, pk):
    form = orderForm()
    item = product.objects.get(pk = pk)
    if request.method == 'POST':
        form = orderForm(request.POST)
        current_user = request.user
        email = request.POST.get('email')
        if (email == current_user.email):
            user_email = current_user
            quantity = 1
            product_id = item
            purchase_date = datetime.date.today()
            my_order = order(user_email = user_email, quantity = quantity, product_id = product_id, purchase_date=purchase_date)
            my_order.save()



    
    product_dict = {'product':item , 'form': form}
    return render(request,'storefront/buy_page.html', context = product_dict)

