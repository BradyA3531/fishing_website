from django.urls import path
from storefront import views


urlpatterns = [
    path('', views.storefront_view, name ="storefront" ),
    path('<int:pk>/', views.item_detail_view, name = "item_detail")
]