# Generated by Django 3.2.18 on 2023-06-24 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsApp', '0015_auto_20230624_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='comp_off_leave',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leave',
            name='encashment_leave',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leave',
            name='paid_leave_balance',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='leave',
            name='total_casual_leaves',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leave',
            name='total_paid_leaves',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='leave',
            name='used_paid_leaves',
            field=models.IntegerField(default=0),
        ),
    ]
