from django.db import models
from datetime import date, datetime


# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255)


class Houses(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)


class Payments(models.Model):
    number = models.IntegerField()
    month = models.CharField(max_length=255)
    amount = models.IntegerField()
    facilitator = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)


class Notices(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    date = models.DateField(default=date.today)
