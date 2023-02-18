from datetime import timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone

from subscription.models import Subscription
from .models import Invoice


class Scheduler():
    scheduler = BackgroundScheduler()

    @classmethod
    def CreateInvoice(self, subscriptionid):
        subscription = Subscription.objects.get(id=subscriptionid)
        customer = subscription.customer
        if customer.credit >= subscription.price and subscription.isactive == True:
            Invoice.objects.create(customer=customer, amount=subscription.price,
                                   start_time=timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
                                   end_time=(timezone.now() + timedelta(seconds=10)).strftime("%Y-%m-%d %H:%M:%S"))
            customer.credit = customer.credit - subscription.price
            customer.save()
        else:
            self.scheduler.pause_job(str(subscriptionid))

    @classmethod
    def addjob(self, subid):
        self.scheduler.add_job(lambda: self.CreateInvoice(subid), 'interval', seconds=30, id=str(subid))

    @classmethod
    def resumejob(self, subid):
        self.scheduler.resume_job(str(subid))
