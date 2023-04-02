from django.db import models

# Create your models here.


class Electronic_detail(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    availability = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.name
