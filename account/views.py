from django.shortcuts import render
from .forms import accountForm

# Create your views here.

#Reminder: Add model stuff later for username/email and password login
def account_view(request):
    return render(request,'account/account.html')

#Reminder: Add model stuff later for username/email and password login
def login_view(request):
    return render(request,'account/login.html')

def register_view(request):
    form = accountForm()
    
    if request.method =='POST':
        form = accountForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form' : form}
    return render(request, 'account/register.html', context)