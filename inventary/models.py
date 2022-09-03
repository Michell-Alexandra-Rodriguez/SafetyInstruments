from django.db import models

from generalvalidations.database_validations import should_be_alphabetic, \
    characters_size_should_be_grater_than_two, \
    category_size_should_be_greater_than_four, state_product_should_be_greater_than_four, is_number, \
    cellphone_number_size_is_ten, identification_number_size_should_be_greater_than_seven, \
    should_not_have_spaces, should_not_have_special_characters
from user.models import IdentificationType


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            validators=[should_be_alphabetic, category_size_should_be_greater_than_four,
                                        should_not_have_special_characters])

    def __str__(self):
        return self.name


class StateProduct(models.Model):
    state = models.CharField(max_length=12, unique=True,
                             validators=[should_be_alphabetic, state_product_should_be_greater_than_four,
                                         should_not_have_special_characters, should_not_have_spaces])

    def __str__(self):
        return self.state


class Supplier(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            validators=[characters_size_should_be_grater_than_two])
    email = models.EmailField(max_length=155, unique=True)
    cellphone = models.CharField(max_length=10, validators=[is_number, cellphone_number_size_is_ten])
    address = models.CharField(max_length=200)
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.PROTECT)
    identification_number = models.CharField(max_length=10,
                                             validators=[
                                                 is_number,
                                                 identification_number_size_should_be_greater_than_seven
                                             ])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=70, validators=[characters_size_should_be_grater_than_two])
    description = models.CharField(max_length=255)
    price_by_unity = models.PositiveIntegerField()
    quantity = models.PositiveSmallIntegerField()
    warranty = models.IntegerField()
    date_arrival = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    state_product = models.ForeignKey(StateProduct, on_delete=models.PROTECT)
    picture = models.ImageField(upload_to='inventary/picture', blank=True, null=True)

    def __str__(self):
        return self.name
