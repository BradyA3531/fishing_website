from django.contrib import admin
from.models import product
from.models import order
from account.models import registered_user
# Register your models here.

admin.site.register(product)
admin.site.register(registered_user)
admin.site.register(order)