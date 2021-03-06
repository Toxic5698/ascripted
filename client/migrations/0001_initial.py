# Generated by Django 3.2.9 on 2022-07-11 14:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, unique=True, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='phone number')),
                ('id_number', models.CharField(blank=True, max_length=12, null=True, verbose_name='id number')),
                ('vat_number', models.CharField(blank=True, max_length=12, null=True, verbose_name='vat number')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='debt')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='WorkSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('causa', models.CharField(max_length=255, verbose_name='causa')),
                ('reward', models.IntegerField(verbose_name='reward')),
                ('total_reward', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='total reward')),
                ('total_other_task_expense', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='total other task expense')),
                ('total_expense', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='total expense')),
                ('note', models.CharField(blank=True, max_length=1000, null=True, verbose_name='note')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worksheets', to='client.profile', verbose_name='profile')),
            ],
            options={
                'verbose_name': 'WorkSheet',
                'verbose_name_plural': 'WorkSheets',
            },
        ),
        migrations.CreateModel(
            name='WorkTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1000, verbose_name='subject')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='date')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='duration')),
                ('start_task', models.TimeField(blank=True, null=True, verbose_name='begin of task')),
                ('end_task', models.TimeField(blank=True, null=True, verbose_name='end of task')),
                ('task_reward', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='task reward')),
                ('other_expense_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='other expense amount')),
                ('other_expense_note', models.CharField(blank=True, max_length=255, null=True, verbose_name='other expense note')),
                ('worksheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_tasks', to='client.worksheet', verbose_name='worksheet')),
            ],
            options={
                'verbose_name': 'WorkTask',
                'verbose_name_plural': 'WorkTasks',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('role', models.CharField(max_length=255, verbose_name='role')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='persons', to='client.profile', verbose_name='profile')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='amount')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to='client.profile', verbose_name='profile')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=20, verbose_name='account')),
                ('bank_id', models.CharField(max_length=4, verbose_name='bank_id')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bankaccounts', to='client.profile', verbose_name='profile')),
            ],
            options={
                'verbose_name': 'Bank Account',
                'verbose_name_plural': 'Bank Accounts',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255, verbose_name='street')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('post_number', models.IntegerField(verbose_name='post_number')),
                ('note', models.CharField(max_length=1000, verbose_name='note')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='client.profile', verbose_name='profile')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
