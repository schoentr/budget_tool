from django.test import TestCase, Client
from ..budget_tool_project.factories import (
    Budget,BudgetFactory,Transaction,TransactionFactory,User,UserFactory
)


class TestBudgetViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.c = Client()

    def test_denied_if_no_login(self):
        res = self.c.get('/budgets/budget', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_view_list_when_logged_in(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        category = BudgetFactory(user=self.user)
        res = self.c.get('/budgets/budget')

        self.assertIn(category.name.encode(), res.content)

    def test_lists_only_owned_categories(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        own_budget = BudgetFactory(user=self.user)
        other_budget = BudgetFactory()

        res = self.c.get('/budgets/budget')

        self.assertIn(own_budget.name.encode(), res.content)
        self.assertNotIn(other_budget.name.encode(), res.content)

    def test_transaction_listed_in_view(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )
        budget = BudgetFactory(user=self.user)
        transaction = TransactionFactory(budget=budget)
        res = self.c.get('/budgets/budget')

        self.assertIn(transaction.description.encode(), res.content)


class TestBudgetCreateViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.c = Client()

    def test_create_view_adds_new_category(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        form_data = {
            'name': 'Test Budget',
            'total_budget': 123.45
        }

        res = self.c.post('/budgets/budget/add', form_data, follow=True)
        self.assertIn(b'Test Budget', res.content)


class TestTransactionCreateViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()

        self.budget = BudgetFactory(user=self.user)

        self.c = Client()

    def test_create_view_adds_new_transaction(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        form_data = {
            'description': 'Tacos',
            'amount': 12.00,
            'budget': self.budget.id
        }

        res = self.c.post('/budgets/transaction/add', form_data, follow=True)

        # Confirms the record was retrieved from the database and presented in the view
        self.assertIn(b'Tacos', res.content)
