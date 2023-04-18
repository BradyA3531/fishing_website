from django.urls import path
from shoppingcart import views

urlpatterns = [
    path('shopping cart', views.shoppingcart_view, name = "shoppingcart")
]