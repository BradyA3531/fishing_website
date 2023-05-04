from django.shortcuts import render, redirect
from .forms import accountForm
from .forms import loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Account
from storefront.models import product
from django.contrib import messages
from storefront.models import order



# Create your views here.

#Reminder: Add model stuff later for username/email and password login
def account_view(request):
    current_user = request.user
    orders = order.objects.filter(user_email = current_user.id)
    
    account_dict = {'account': current_user, 'order': orders}
    return render(request,'account/account.html', context = account_dict)

#Reminder: Add model stuff later for username/email and password login
def login_view(request):
    if request.method == 'POST':
        inputEmail = request.POST.get('email')
        inputPassword = request.POST.get('password')
        user = authenticate(request, email = inputEmail, password = inputPassword)
        if user is not None:
            login(request, user)
            print(user)
            return redirect('storefront')
        else:
            messages.success(request, "Invalid Email AND OR Password")
    return render(request,'account/login.html')

def register_view(request):
    form = accountForm() 
    if request.method =='POST':
        form = accountForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            fname = request.POST['fname']
            lname = request.POST['lname']
            password = request.POST['password']
            city = request.POST['city']
            addressline1 = request.POST['addressline1']
            state = request.POST['state']
            zipcode = request.POST['zipcode']
            sec_answer = request.POST['sec_answer']
            account = Account.objects.create_user(email, fname, lname, addressline1, city, state, zipcode, sec_answer, password)
            account.save()
            messages.success(request, "Account was created")
            return redirect('login')
        else:
            messages.success(request, "Account was not created")
            
    context = {'form' : form}
    return render(request, 'account/register.html', context)


def signout(request):
    logout(request)
    messages.success(request,"you were succesfully logged out")
    return redirect('login')
    