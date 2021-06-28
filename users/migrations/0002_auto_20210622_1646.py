# Generated by Django 3.2.2 on 2021-06-22 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='whitelist',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='whitelist',
            name='userid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]