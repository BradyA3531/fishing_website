from django.forms import ModelForm
from .models import Account

class accountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'password', 'fname', 'lname', 'addressline1', 'city', 'state', 'zipcode', 'sec_answer']
        