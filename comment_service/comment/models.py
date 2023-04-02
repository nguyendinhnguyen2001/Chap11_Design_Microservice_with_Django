from django.db import models

# Create your models here.

class Comment(models.Model):
    email = models.CharField(max_length=200)
    product_id = models.IntegerField()
    comment = models.TextField()
    time_posted=models.CharField(max_length=200)
    def __str__(self):
        return self.comment
    