from django.urls import path
from account import views

urlpatterns = [
    path('account', views.account_view, name = "account"),
    path('login', views.login_view, name = "login" )
]