import factory
from django.contrib.auth.models import User
from budgets.models import Budget, Transaction


class UserFactory(factory.django.DjangoModelFactory):
    """Create a test user for writing tests."""

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BudgetFactory(factory.django.DjangoModelFactory):
    """Create a test category for writing tests."""

    class Meta:
        model = Budget

    user = factory.SubFactory(UserFactory)
    name= factory.Faker('word')
    total_budget = 123.45
    remaining_budget = 123.00


class TransactionFactory(factory.django.DjangoModelFactory):
    """Create a test card for writing tests."""

    class Meta:
        model = Transaction

    budget = factory.SubFactory(BudgetFactory)

    amount = 11.00
    description = factory.Faker('paragraph')
