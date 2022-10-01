from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Users(models.Model):
    First_Name = models.CharField(max_length= 50)
    Last_Name = models.CharField(max_length= 50)
    Email = models.EmailField(max_length= 50, unique=True)
    Password = models.CharField(max_length= 50)
    Confirm_Password = models.CharField(max_length= 50)
    Phone_Number = PhoneNumberField(null=False, blank=False, unique=True)
    Profile_Picture = models.ImageField(upload_to='photos/%y/%m/%d', blank=True, null=True)

