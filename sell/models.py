from django.db import models
from user.models import Client
from django.contrib.auth.models import User
from inventary.models import Product


class PaymentType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sell(models.Model):
    date_sell = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product)
