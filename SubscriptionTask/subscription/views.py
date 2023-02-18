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
        subscription = Subscription.objects.get(id = pk)
        serializer = SubscriptionEditActivationSerializer(data=request.data)
        if serializer.is_valid():
            subscription.isactive = request.data.get('isactive')
            subscription.save()
            if subscription.isactive == True:
                Scheduler.resumejob(pk)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)