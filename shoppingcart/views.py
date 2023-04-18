from django.shortcuts import render

# Create your views here.

def shoppingcart_view(request):
    return render(request, 'shoppingcart/shoppingcart.html')