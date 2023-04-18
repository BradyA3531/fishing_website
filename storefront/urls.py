from django.urls import path
from storefront import views


urlpatterns = [
    path('', views.storefront_view, name ="storefront" ),
]