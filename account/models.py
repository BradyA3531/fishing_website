from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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

class MyAccountManager(BaseUserManager):
    def create_user(self, email, fname, lname, addressline1, city, state, zipcode, sec_answer, password = None):
        if not email:
            raise ValueError("users must have an email address")
        
        user = self.model(
            email = self.normalize_email(email),
            fname = fname,
            lname = lname,
            addressline1 = addressline1,
            city = city,
            state = state,
            zipcode = zipcode, 
            sec_answer = sec_answer
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, fname, lname, addressline1 ,password, city, state, zipcode, sec_answer):
        user = self.create_user(
            email = self.normalize_email(email),
            fname = fname,
            lname = lname,
            addressline1=addressline1,
            password = password,
            city = city,
            state = state,
            zipcode = zipcode,
            sec_answer = sec_answer
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 50)
    addressline1 = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(null=False, max_length=20)
    sec_answer = models.CharField(max_length=50)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname', 'addressline1', 'city', 'state', 'zipcode', 'sec_answer']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
   
    





