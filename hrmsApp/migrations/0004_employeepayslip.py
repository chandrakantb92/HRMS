# Generated by Django 4.2.1 on 2023-06-16 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsApp', '0003_auto_20230601_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeePaySlip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slip_num', models.IntegerField(default=0)),
                ('month', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=30)),
                ('basic', models.CharField(default='0', max_length=20)),
                ('hra', models.CharField(default='0', max_length=20)),
                ('travel_allowence', models.CharField(default='0', max_length=20)),
                ('medical_allowence', models.CharField(default='0', max_length=20)),
                ('other_allowence', models.CharField(default='0', max_length=20)),
                ('arrears', models.CharField(default='0', max_length=20)),
                ('leave_encashment', models.CharField(default='0', max_length=20)),
                ('bonus', models.CharField(default='0', max_length=20)),
                ('provident_fund', models.CharField(default='0', max_length=20)),
                ('esic', models.CharField(default='0', max_length=20)),
                ('professional_tax', models.CharField(default='0', max_length=20)),
                ('other_charges', models.CharField(default='0', max_length=20)),
                ('tds', models.CharField(default='0', max_length=20)),
                ('advances', models.CharField(default='0', max_length=20)),
                ('total_deduction', models.CharField(default='0', max_length=20)),
                ('total_earning', models.CharField(default='0', max_length=20)),
                ('net_pay', models.CharField(default='0', max_length=20)),
                ('issued_date', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('created_by', models.CharField(max_length=50)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrmsApp.employee')),
            ],
            options={
                'db_table': 'emp_payslip',
            },
        ),
    ]
