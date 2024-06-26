# Generated by Django 5.0.6 on 2024-06-24 16:46

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_delete_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_by', to='book.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
