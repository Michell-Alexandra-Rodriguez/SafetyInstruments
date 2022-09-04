from django.contrib.auth.models import User
from django.db import models

from generalvalidations.database_validations import characters_size_should_be_grater_than_two, \
    should_be_alphabetic, should_not_have_spaces, is_number, cellphone_number_size_is_ten, \
    identification_number_size_should_be_greater_than_seven, should_not_have_special_characters, \
    characters_size_should_be_grater_than_one, should_not_have_accents


class IdentificationType(models.Model):
    type = models.CharField(max_length=4, unique=True, validators=[
        characters_size_should_be_grater_than_one, should_be_alphabetic, should_not_have_spaces,
        should_not_have_special_characters, should_not_have_accents
    ])

    def __str__(self):
        return self.type


class UserAdditionalInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=10, validators=[is_number, cellphone_number_size_is_ten])
    picture = models.ImageField(upload_to='user/picture', blank=True, null=True)
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.PROTECT)
    identification_number = models.CharField(max_length=10,
                                             validators=[
                                                 is_number,
                                                 identification_number_size_should_be_greater_than_seven
                                             ])

    def __str__(self):
        return self.user.username


class Client(models.Model):
    name = models.CharField(max_length=50, validators=[
        should_be_alphabetic, characters_size_should_be_grater_than_two, should_not_have_special_characters
    ])
    last_name = models.CharField(max_length=50, validators=[
        should_be_alphabetic, characters_size_should_be_grater_than_two, should_not_have_special_characters
    ])
    email = models.EmailField(max_length=90, unique=True)
    address = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=10, validators=[is_number, cellphone_number_size_is_ten])
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.PROTECT)
    identification_number = models.CharField(max_length=10,
                                             validators=[
                                                 is_number,
                                                 identification_number_size_should_be_greater_than_seven
                                             ])

    def __str__(self):
        return self.name
