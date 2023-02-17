from django.urls import path
from .views import RegisterCustomer,IncreaseCredit
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
      path('register/', RegisterCustomer.as_view()),
      path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
      path('increasecredit/', IncreaseCredit.as_view()),
]