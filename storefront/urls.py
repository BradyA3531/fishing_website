from django.urls import path
from storefront import views


urlpatterns = [
    path('', views.storefront_view, name ="storefront" ),
    path('<int:pk>/', views.item_detail_view, name = "item_detail"),
    path('<int:pk>/buy', views.buy_page_view, name = "buy_page"),
    path('lure/', views.filterByLures, name = "filter_by_lures"),
    path('rods/', views.filterByRods, name = "filter_by_rods"),
    path('bait/', views.filterByBait, name = "filter_by_bait"),
    path('misc/', views.filterByMisc, name = "filter_by_misc"),
]