from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from invoice.schedulers import Scheduler
from subscription.models import Subscription
from .models import Customer
from .serializer import CustomerSerializer,IncreaseCreditCustomerSerializer


class RegisterCustomer(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return Response({
                "customer": CustomerSerializer(customer).data,
                "message": "Customer Created Successfully.  Now perform Login to get your token",
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncreaseCredit(APIView):
    def put(self,request):
        customer = Customer.objects.get(id = request.user.id)
        serializer = IncreaseCreditCustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer.credit += request.data.get("credit")
            customer.save()
            subs = Subscription.objects.filter(customer=customer)
            for s in subs:
                if s.price <= customer.credit:
                    Scheduler.resumejob(s.id)
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)