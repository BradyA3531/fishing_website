from django.db import models

# Create your models here.

#product model, representing items that will be sold within a store
class product(models.Model):
        product_id = models.AutoField(primary_key=True)
        product_name = models.CharField(max_length=50)
        product_desc = models.CharField(max_length =75)
        price = models.FloatField()
        product_type = models.CharField(max_length=50)
        on_sale = models.BooleanField()
        quantity = models.IntegerField()
        img = models.ImageField(null = True, blank = True)

        def __str__(self):
                        return self.product_name
        @property
        def imageURL(self):
                try:
                        url = self.img.url
                except:
                        url = ''
                return url


#order model
class order(models.Model):
        order_id = models.AutoField(primary_key=True)
        user_id = models.ForeignKey("account.Account", verbose_name=("email"), on_delete=models.CASCADE)
        quantity = models.IntegerField(null=False)
        product_id = models.ForeignKey("storefront.product", verbose_name=("product_id"), on_delete=models.CASCADE)
        purchase_date = models.DateField(auto_created=True)

