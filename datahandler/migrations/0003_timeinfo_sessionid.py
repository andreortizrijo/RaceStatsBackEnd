# Generated by Django 3.2.2 on 2021-06-16 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datahandler', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeinfo',
            name='sessionid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='datahandler.sessioninfo'),
        ),
    ]