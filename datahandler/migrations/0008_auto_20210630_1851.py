# Generated by Django 3.2.2 on 2021-06-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahandler', '0007_auto_20210628_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinfo',
            name='brakepedal',
            field=models.FloatField(max_length=255),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='clutchpedal',
            field=models.FloatField(max_length=255),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='gaspedal',
            field=models.FloatField(max_length=255),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='gear',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='rpm',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='speedkmh',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='steerangle',
            field=models.FloatField(max_length=255),
        ),
    ]
