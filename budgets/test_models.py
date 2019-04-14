from django.test import TestCase
from ..budget_tool_project.factories import UserFactory, BudgetFactory, TransactionFactory


class TestBudgetModels(TestCase):
    def setUp(self):
        self.budget = BudgetFactory(
            name='Test Name',
            total_budget=123.45,
            remaining_budget=123.00,
        )

    def test_budget_model_attrs(self):
        self.assertEqual(self.budget.name, 'Test Name')
        self.assertEqual(self.budget.total_budget, 123.45)
        self.assertEqual(self.budget.remaining_budget, 123.00)

class TestTransactionModels(TestCase):
    def setUp(self):
        self.transaction = TransactionFactory(
            status = 'Withdrawal',
            amount = 12.00,
            description = "Cold Beer"
        )
    def test_transaction_model(self):
        self.assertEqual(self.transaction.amount, 12.00)
        self.assertEqual(self.transaction.status, 'Withdrawal')
        self.assertEqual(self.transaction.description, 'Cold Beer')

