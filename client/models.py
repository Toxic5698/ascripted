from django.db import models
from django.db.models import (CharField, EmailField, ForeignKey, IntegerField, DecimalField,
                              FloatField, DateField, TimeField, Sum)

from datetime import *


class Profile(models.Model):
    name = CharField(max_length=1000, unique=True)
    email = EmailField()
    phone_number = CharField(max_length=255, null=True, blank=True)
    id_number = CharField(max_length=12, null=True, blank=True)
    vat_number = CharField(max_length=12, null=True, blank=True)
    #created
    #updated

    debt = DecimalField(null=True, blank=True, max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

    def clean(self):
        payments = self.payments.all().aggregate(Sum('amount'))['amount__sum'] or 0
        total_expense = self.worksheets.all().aggregate(Sum('total_expense'))['total_expense__sum'] or 0
        self.debt = total_expense - payments

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Address(models.Model):
    profile = ForeignKey(Profile, on_delete=models.CASCADE, related_name='addresses', null=True, blank=True)
    street = CharField(max_length=255)
    city = CharField(max_length=100)
    post_number = IntegerField()
    note = CharField(max_length=1000)

    class Meta:
        verbose_name_plural = 'Addresses'


class BankAccount(models.Model):
    profile = ForeignKey(Profile, on_delete=models.CASCADE, related_name='bankaccounts', null=True, blank=True)
    account = IntegerField()
    bank_id = CharField(max_length=4)


class Person(models.Model):
    profile = ForeignKey(Profile, on_delete=models.SET_NULL, related_name='persons', null=True)
    title = CharField(max_length=255)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    role = CharField(max_length=255)


class WorkSheet(models.Model):
    profile = ForeignKey(Profile, related_name='worksheets', on_delete=models.SET_NULL, null=True)
    causa = CharField(max_length=255)

    reward = IntegerField()
    total_reward = DecimalField(null=True, blank=True, max_digits=12, decimal_places=2)
    total_other_task_expense = DecimalField(null=True, blank=True, max_digits=12, decimal_places=2)
    total_expense = DecimalField(null=True, blank=True, max_digits=12, decimal_places=2)

    note = CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.causa} - {self.profile}"

    def clean(self):
        self.total_reward = round(self.work_tasks.all().aggregate(Sum('task_reward'))['task_reward__sum'], 2)
        self.total_other_task_expense = round(self.work_tasks.all()
                                              .aggregate(Sum('other_expense_amount'))['other_expense_amount__sum'], 2)
        self.total_expense = self.total_reward + self.total_other_task_expense

    def save(self, *args, **kwargs):
        super(WorkSheet, self).save(*args, **kwargs)


class WorkTask(models.Model):
    worksheet = ForeignKey(WorkSheet, on_delete=models.CASCADE, related_name='work_tasks')
    subject = CharField(max_length=1000)
    date = DateField(default=datetime.now)
    duration = IntegerField()
    start_task = TimeField(null=True, blank=True)
    end_task = TimeField(null=True, blank=True)
    task_reward = DecimalField(null=True, blank=True, max_digits=12, decimal_places=2)
    other_expense_amount = DecimalField(null=True, blank=True, max_digits=12, decimal_places=2)
    other_expense_note = CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.subject}, {self.date} ({self.worksheet})"

    def get_task_reward(self):
        task_reward = self.duration * (self.worksheet.reward/60)
        return round(task_reward, 2)

    def save(self, *args, **kwargs):
        self.task_reward = self.get_task_reward()
        if self.start_task and self.end_task:
            self.duration = self.end_task - self.start_task
        super(WorkTask, self).save(*args, **kwargs)


class Payments(models.Model):
    profile = ForeignKey(Profile, related_name='payments', on_delete=models.SET_NULL, null=True)
    date = DateField()
    amount = FloatField()

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return f'{self.profile} - {self.amount} - {self.date}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.profile.save()


