from django.db import models
from user.models import IdentificationType


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class StateProduct(models.Model):
    state = models.CharField(max_length=10)

    def __str__(self):
        return self.state


class Supplier(models.Model):
    name = models.CharField(max_length=45)
    cellphone = models.CharField(max_length=15)
    address = models.CharField(max_length=70)
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.PROTECT)
    identification_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    warranty = models.IntegerField()
    date_arrival = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    state_product = models.ForeignKey(StateProduct, on_delete=models.PROTECT)
    picture = models.ImageField(upload_to='inventary/picture', blank=True, null=True)

    def __str__(self):
        return self.name
