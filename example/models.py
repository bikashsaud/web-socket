# Create your models here.
from django.conf import settings
from django.db import models


class LoggedInUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='logged_in_user')




class Book(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    summery = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

        