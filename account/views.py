from django.shortcuts import render, redirect
from .forms import accountForm
from .forms import loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Account

# Create your views here.

#Reminder: Add model stuff later for username/email and password login
def account_view(request):
    return render(request,'account/account.html')

#Reminder: Add model stuff later for username/email and password login
def login_view(request):

    if request.method == 'POST':
        inputEmail = request.POST.get('email')
        inputPassword = request.POST.get('password')
        account = Account.objects.get(email = inputEmail)
        if(inputPassword ==  account.password):
            print(inputPassword)
            print(account.password)
            return redirect('storefront')
    

    return render(request,'account/login.html')

def register_view(request):
    form = accountForm()
    
    if request.method =='POST':
        form = accountForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')

    context = {'form' : form}
    return render(request, 'account/register.html', context)