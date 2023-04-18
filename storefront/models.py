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

#order model
  