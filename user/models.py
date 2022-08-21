from django.db import models
from django.contrib.auth.models import User


class IdentificationType(models.Model):
    type = models.CharField(max_length=45)

    def __str__(self):
        return self.type


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=15)
    picture = models.ImageField(upload_to='user/picture', blank=True, null=True)
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.PROTECT)
    identification_number = models.IntegerField()

    def __str__(self):
        return self.user


class Client(models.Model):
    people = models.ForeignKey(Profile, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.people)
