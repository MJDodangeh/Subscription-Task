from django.urls import path
from .views import InvoiceList,InvoicesStatistics

urlpatterns = [
      path('list', InvoiceList.as_view()),
      path('statistics', InvoicesStatistics.as_view())
]