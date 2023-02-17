from django.contrib.auth.models import User, AbstractUser
from django.db import models

class Customer(AbstractUser):
    credit = models.IntegerField()