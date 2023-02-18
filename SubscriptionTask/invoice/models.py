from django.db import models

from customer.models import Customer


class Invoice(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
