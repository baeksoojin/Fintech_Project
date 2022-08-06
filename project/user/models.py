from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []