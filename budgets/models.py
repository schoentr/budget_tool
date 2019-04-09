
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db import models


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField(max_length=180, default='Untitled')
    total_budget = models.FloatField(blank=True, null=True)
    remaining_budget = models.FloatField(blank=True, null=True)

    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __repr__(self):
        return '<Category: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)


class Transaction(models.Model):
    budget=models.ForeignKey(Budget,on_delete=models.CASCADE,related_name=User_id)
    amount= models.FloatField(blank=Ture, null=False)
    description= models.CharField(max_length=256, default='Untitied')
type: Choices(withdrawal, deposit)





@receiver(models.signals.post_save, sender=Card)
def set_card_completed_date(sender, instance, **kwargs):
    """Update the date completed if completed."""
    if instance.date_completed == 'Complete' and not instance.date_completed:
        instance.date_completed = timezone.now()
        instance.save()