from django.db import models

class registered_user(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(null=False, max_length=25)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    addressline1 = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(null=False, max_length=20)
    signup_date = models.DateField(auto_created=True)
    sec_answer = models.CharField(max_length=50)

   




