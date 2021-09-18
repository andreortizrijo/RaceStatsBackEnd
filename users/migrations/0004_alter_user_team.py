# Generated by Django 3.2.2 on 2021-09-16 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_alter_team_owner'),
        ('users', '0003_user_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='team',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.team'),
        ),
    ]
