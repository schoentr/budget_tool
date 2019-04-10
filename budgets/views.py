from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView,CreateView
from .models import Transaction, Budget
from .forms import TransactionForm, BudgetForm
from django.urls import reverse_lazy

# Create your views here.

class BudgetView(LoginRequiredMixin,ListView):
    template_name = 'budget/budget_list.html'
    context_object_name = 'budgets'
    login_url=reverse_lazy('login')

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['transactions']= Transaction.objects.filter(budget__user__username=self.request.user.username)
        return context

class TransactionView(LoginRequiredMixin,DetailView):
    template_name='budget/transaction_detail.html'
    model= Transaction
    context_object_name='transaction'
    login_url=reverse_lazy('login')
    pk_url_kwarg ='id'

    def get_queryset(self):
        return Transaction.objects.filter(budget__user__username=self.request.user.username)

class TransactionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'budget/transaction_create.html'
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('budget_view')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validate form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class BudgetCreateView(LoginRequiredMixin, CreateView):
    template_name = 'budget/budget_create.html'
    model = Budget
    form_class = BudgetForm
    success_url = reverse_lazy('budget_view')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validate form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)

