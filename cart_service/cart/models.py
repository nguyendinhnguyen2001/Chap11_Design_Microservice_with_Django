from django.db import models

# Create your models here.
class Cart(models.Model):
    uname=models.CharField(max_length=200)
    product_id=models.IntegerField()
    quantity=models.IntegerField()
    def __str__(self):
        return self.uname
    