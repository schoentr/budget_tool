# Generated by Django 2.2 on 2019-04-09 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0006_auto_20190409_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='remaining_budget',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='budget',
            name='total_budget',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(blank=True),
        ),
    ]
