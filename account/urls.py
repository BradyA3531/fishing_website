from django.urls import path
from account import views

urlpatterns = [
    path('', views.account_view, name = "account"),
    path('login/', views.login_view, name = "login" ),
    path('register/', views.register_view, name = "register"),
    path('logout/', views.signout, name="logout"),
    
]