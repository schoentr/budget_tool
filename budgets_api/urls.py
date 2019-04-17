from django.urls import path
from .views import UserAPIView, RegisterApiView, BudgetListAPIView, BudgetDetailAPIView, TransactionDetailAPIView,TransactionListAPIView
from rest_framework.authtoken import views




urlpatterns = [
    path('budget/', BudgetListAPIView.as_view() , name = 'budget_list_api'),
    path('budget/<int:pk>', BudgetDetailAPIView.as_view() , name = 'budget_detail_api'),
    path('transaction/', TransactionListAPIView.as_view() , name = 'transaction_list_api'),
    path('transaction/<int:pk>', TransactionDetailAPIView.as_view() , name = 'transaction_detail_api'),
    path('user/<int:pk>', UserAPIView.as_view(), name='user_detail'),
    path('register', RegisterApiView.as_view(), name='register'),
    path('login', views.obtain_auth_token),
]
