# Generated by Django 4.2.1 on 2023-06-16 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsApp', '0004_otpauthentication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeeducationdetails',
            name='pg_stream',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employeeeducationdetails',
            name='ug_stream',
            field=models.CharField(max_length=50),
        ),
    ]