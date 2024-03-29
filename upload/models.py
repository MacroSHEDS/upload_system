from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    DATA_PRODUCTS = [
        ('stream chemistry', 'stream chemistry'),
        ('stream discharge', 'stream discharge'),
        ('precipitation chemistry', 'precipitation chemistry'),
        ('precipitation volume', 'precipitation volume'),
    ]

    # fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prod_id = models.BigAutoField(primary_key=True)
    # prod_select = models.BooleanField()
    prod_name = models.CharField(max_length=50,
                                 choices = DATA_PRODUCTS)
    def prod_status(self):
        return self.prod_select

    def __str__(self):
        return self.prod_name

