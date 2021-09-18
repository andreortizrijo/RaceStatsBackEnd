# Generated by Django 3.2.2 on 2021-09-16 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_alter_team_owner'),
        ('users', '0002_auto_20210622_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='teams.team'),
        ),
    ]