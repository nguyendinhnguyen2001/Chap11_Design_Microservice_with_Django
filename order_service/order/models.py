from django.db import models

# Create your models here.
class Order(models.Model):
    cart_uname=models.CharField(max_length=200)
    cart_product_id=models.IntegerField()
    cart_quantity=models.IntegerField()
    cart_total=models.FloatField(default=0)
    order_timeed=models.CharField(max_length=200)
    def __str__(self):
        return self.cart_uname