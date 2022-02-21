from django.db import models
from django.db.models import (BooleanField,  CharField, EmailField, ForeignKey,
                              ManyToManyField, OneToOneField, IntegerField, SET_NULL,
                              FloatField, Q, DateField, TimeField)

from datetime import *


class Profile(models.Model):
    name = CharField(max_length=1000, unique=True)
    email = EmailField()
    phone_number = CharField(max_length=255, null=True, blank=True)
    id_number = CharField(max_length=12, null=True, blank=True)
    vat_number = CharField(max_length=12, null=True, blank=True)
    #created
    #updated

    def __str__(self):
        return self.name


class Address(models.Model):
    profile = ForeignKey(Profile, on_delete=models.CASCADE, related_name='address', null=True, blank=True)
    street = CharField(max_length=255)
    city = CharField(max_length=100)
    post_number = IntegerField()
    note = CharField(max_length=1000)


class BankAccount(models.Model):
    profile = ForeignKey(Profile, on_delete=models.CASCADE, related_name='bankaccount', null=True, blank=True)
    account = IntegerField()
    bank_id = IntegerField()


class Person(models.Model):
    profile = ForeignKey(Profile, on_delete=models.SET_NULL, related_name='person', null=True)
    title = CharField(max_length=255)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    role = CharField(max_length=255)


class WorkSheet(models.Model):
    profile = ForeignKey(Profile, related_name='profile', on_delete=models.SET_NULL, null=True)
    causa = CharField(max_length=255)

    reward = IntegerField()
    total_expense = FloatField()
    prepaid_expense = FloatField()
    debt = FloatField()

    note = CharField(max_length=1000, null=True, blank=True)

    # def clean(self):
    #
    #
    # def save(self, *args, **kwargs):
    #     self.clean(self)


class WorkTask(models.Model):
    worksheet = ForeignKey(WorkSheet, on_delete=models.CASCADE, related_name='worktask')
    subject = CharField(max_length=1000)
    date = DateField(default=datetime.now)
    duration = IntegerField()
    start_task = TimeField(null=True, blank=True)
    end_task = TimeField(null=True, blank=True)
    task_reward = FloatField()
    other_expense_amount = FloatField(null=True, blank=True)
    other_expense_note = CharField(max_length=255, null=True, blank=True)

    def get_task_reward(self):
        task_reward = self.duration * (self.worksheet.reward/60)
        return task_reward

    def get_duration(self):
        if self.start_task and self.end_task:
            duration = self.end_task - self.start_task
            return duration
        pass

