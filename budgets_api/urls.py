from django.urls import path
from .views import UserAPIView, RegisterApiView, BudgetListAPIView, BudgetDetailAPIView, TransactionDetailAPIView,TransactionListAPIView
from rest_framework.authtoken import views




urlpatterns = [
    path('budget/', BudgetListAPIView , name = 'budget_list_api'),
    path('budget/<int:pk>', BudgetDetailAPIView , name = 'budget_detail_api'),
    path('transaction/', TransactionListAPIView , name = 'transaction_list_api'),
    path('transaction/<int:pk>', TransactionDetailAPIView , name = 'transaction_detail_api'),
    path('user/<int:pk>', UserAPIView.as_view(), name='transaction_detail'),
    path('register', RegisterApiView.as_view(), name='register'),
    path('login', views.obtain_auth_token),
]
