from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Company(models.Model):
    name = models.CharField(max_length=64, default="")
    phone = PhoneNumberField()
    email = models.EmailField(default="")
