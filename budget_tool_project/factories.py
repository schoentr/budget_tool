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
        model = Category

    user = factory.SubFactory(UserFactory)
    total_budget = factory.Faker.numerify(text="####")
    description = factory.Faker('paragraph')


class TransactionFactory(factory.django.DjangoModelFactory):
    """Create a test card for writing tests."""

    class Meta:
        model = Card

    budget = factory.SubFactory(BudgetFactory)

    amount = factory.Faker()
    description = factory.Faker('paragraph')
