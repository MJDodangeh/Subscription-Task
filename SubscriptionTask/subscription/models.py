from django.db import models
from customer.models import Customer

class Subscription(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    isactive = models.BooleanField(default=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
