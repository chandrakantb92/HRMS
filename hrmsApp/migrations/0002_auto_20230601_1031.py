# Generated by Django 3.2.18 on 2023-06-01 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeattendance',
            name='in_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='employeeattendance',
            name='out_time',
            field=models.TimeField(blank=True),
        ),
    ]
