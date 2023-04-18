from django.urls import path
from ownerpage import views

urlpatterns = [
    path('ownerpage',views.ownerpage_view, name = "ownerpage")
]