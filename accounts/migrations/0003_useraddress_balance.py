# Generated by Django 5.0.6 on 2024-06-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]