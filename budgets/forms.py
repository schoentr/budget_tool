from django.forms import ModelForm
from .models import Budget, Transaction


class BudgetForm(ModelForm):
    """User input form for making a new Budget.

    """

    class Meta:
        model = Budget
        fields = ['name', 'total_budget','remaining_budget']


class TransactionForm(ModelForm):
    """User input form for making a new Transaction."""
    class Meta:
        model = Transaction
        fields = ['budget','status', 'amount','description']
