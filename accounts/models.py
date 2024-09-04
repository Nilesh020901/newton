from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class GFG(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELD = []
    objects = UserManager()
