# Generated by Django 3.2.2 on 2021-06-15 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datahandler', '0006_rename_record_id_sessioninfo_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessioninfo',
            name='record',
        ),
    ]
