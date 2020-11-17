from django.db import models
from datetime import datetime


class Seller(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    top_seller = models.BooleanField(default=False)
    trending_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.name