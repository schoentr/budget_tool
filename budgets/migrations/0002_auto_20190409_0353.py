# Generated by Django 2.2 on 2019-04-09 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='date_uploaded',
        ),
    ]
