# Generated by Django 2.2 on 2019-04-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0004_transaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='remaining_budget',
            field=models.FloatField(verbose_name=0.0),
        ),
        migrations.AlterField(
            model_name='budget',
            name='total_budget',
            field=models.FloatField(verbose_name=0.0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(blank=True, verbose_name=0.0),
        ),
    ]
