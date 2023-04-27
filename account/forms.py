from django.forms import ModelForm
from .models import Account
from django import forms

class accountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'password', 'fname', 'lname', 'addressline1', 'city', 'state', 'zipcode', 'sec_answer']
        
        

class loginForm(ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'password']