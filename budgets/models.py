
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models


class Budget(models.Model):
    """This is the model for a budget

    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField(max_length=180, default='Untitled')
    total_budget = models.FloatField()
    remaining_budget = models.FloatField()

    def __repr__(self):
        return '<Budget: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)


class Transaction(models.Model):
    """This is the model for a Transaction

    """


    budget=models.ForeignKey(Budget,on_delete=models.CASCADE,related_name='transactions')
    STATES = (
        ('DEPOSIT','Deposit'),
        ('WITHDRAWAL','Withdrawal'),
    )
    status = models.CharField(
        max_length=16,
        choices=STATES,
        default='Withdrawal'
    )
    amount= models.FloatField(blank=True, null=False)
    description= models.CharField(max_length=256, default='Untitied')
    def __repr__(self):
        return '<Transaction: {} | {}'.format(self.status, self.amount)


