from django.urls import path
from .views import CreateSubscription,EditActivation

urlpatterns = [
      path('create/', CreateSubscription.as_view()),
      path('editactivation/<int:pk>/', EditActivation.as_view()),
]