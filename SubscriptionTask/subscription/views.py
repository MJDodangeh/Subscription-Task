from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import SubscriptionSerializer,SubscriptionEditActivationSerializer
from .models import Subscription
from invoice.schedulers import Scheduler


class CreateSubscription(APIView):
    def post(self,request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["customer"] = request.user
            sub = serializer.save()
            Scheduler.addjob(sub.id)
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditActivation(APIView):
    def put(self,request,pk):
        try:
            subscription = Subscription.objects.get(id = pk)
        except:
            return Response({"detail": "The Subscription Id is incorrect"},status=status.HTTP_400_BAD_REQUEST)
        serializer = SubscriptionEditActivationSerializer(data=request.data)
        if serializer.is_valid():
            if subscription.customer == request.user:
                subscription.isactive = request.data.get('isactive')
                subscription.save()
                if subscription.isactive == True:
                    Scheduler.resumejob(pk)
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response({"detail":"This Subscription Id does not belong to you"},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionList(APIView):
    def get(self,request):
        subscriptions = Subscription.objects.filter(customer=request.user)
        serializer = SubscriptionSerializer(subscriptions,many=True)
        return Response({"subscriptions":serializer.data}, status=status.HTTP_200_OK)