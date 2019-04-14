from django.urls import path
from .views import UserAPIView, RegisterApiView
from rest_framework.authtoken import views




urlpatterns = [
    path('user/<int:pk>', UserAPIView.as_view(), name='transaction_detail'),
    path('register', RegisterApiView.as_view(), name='register'),
    path('login', views.obtain_auth_token),
]
