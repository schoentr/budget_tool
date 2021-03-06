from django.urls import path
from .views import BudgetView, TransactionView,BudgetCreateView,TransactionCreateView

urlpatterns=[
    path('budget',BudgetView.as_view(),name='budget_view'),
    path('transaction/<int:id>',TransactionView.as_view(),name='transaction_detail'),
    path('budget/add', BudgetCreateView.as_view(), name='budget_add'),
    path('transaction/add', TransactionCreateView.as_view(), name='transaction_add'),

]
