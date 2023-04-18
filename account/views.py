from django.shortcuts import render

# Create your views here.

#Reminder: Add model stuff later for username/email and password login
def account_view(request):
    return render(request,'account/account.html')

#Reminder: Add model stuff later for username/email and password login
def login_view(request):
    return render(request,'account/login.html')