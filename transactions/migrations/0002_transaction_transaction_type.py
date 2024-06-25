# Generated by Django 5.0.6 on 2024-06-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Borrow'), (2, 'Return')], null=True),
        ),
    ]
