from django.db import models

# Create your models here.


class Book(models.Model):
    # book_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    auther = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    availability = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publish_Date = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.title
