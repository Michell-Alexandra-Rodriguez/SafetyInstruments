from django.db import models
from user.models import Client
from django.contrib.auth.models import User
from inventary.models import Product
from generalvalidations.database_validations import characters_size_should_be_grater_than_two, \
    should_be_alphabetic, should_not_have_special_characters


class PaymentType(models.Model):
    name = models.CharField(max_length=20, unique=True,
                            validators=[characters_size_should_be_grater_than_two, should_be_alphabetic,
                                        should_not_have_special_characters])

    def __str__(self):
        return self.name


class Sell(models.Model):
    date_sell = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.product)
