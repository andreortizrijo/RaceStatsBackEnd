# Generated by Django 3.2.2 on 2021-06-30 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahandler', '0008_auto_20210630_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinfo',
            name='brakepedal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='clutchpedal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='gaspedal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='gear',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='rpm',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='speedkmh',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='steerangle',
            field=models.FloatField(),
        ),
    ]