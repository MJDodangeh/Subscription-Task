from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Invoice
from .serializer import InvoiceSerializer


class InvoiceList(APIView):
    def get(self,request):
        invoices = Invoice.objects.filter(customer=request.user)
        serializer = InvoiceSerializer(invoices,many=True)
        return Response({"invoices":serializer.data}, status=status.HTTP_200_OK)

class InvoicesStatistics(APIView):
    def get(self,request):
        invoices = Invoice.objects.filter(customer=request.user)
        number_of_invoices = len(invoices)
        total_cost_amount = 0
        for i in invoices:
            total_cost_amount += i.amount
        return Response({"number_of_invoices":number_of_invoices,"total_cost_amount":total_cost_amount}, status=status.HTTP_200_OK)