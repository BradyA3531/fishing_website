from .models import order
from django.forms import ModelForm

class orderForm(ModelForm):
    class Meta:
        model = order
        fields = ['user_email']