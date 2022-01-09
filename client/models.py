from django.db import models
from django.db.models import (BooleanField,  CharField, EmailField, ForeignKey,
                              ManyToManyField, OneToOneField, IntegerField, SET_NULL,
                              FloatField, Q, DateField, TimeField)

from datetime import *


class Address(models.Model):
    street = CharField(max_length=255)
    city = CharField(max_length=100)
    post_number = IntegerField()
    note = CharField(max_length=1000)


class Person(models.Model):
    title = CharField(max_length=255)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    role = CharField(max_length=255)


class BankNumber(models.Model):
    number = IntegerField()
    bank_id = IntegerField()


class Profile(models.Model):
    name = CharField(max_length=1000, unique=True)
    address = ForeignKey(Address, related_name='profile', on_delete=models.CASCADE)
    email = EmailField()
    phone_number = CharField(max_length=255, null=True, blank=True)
    id_number = IntegerField(null=True, blank=True)
    vat_number = CharField(max_length=12, null=True, blank=True)
    bank_number = ForeignKey(BankNumber, related_name='profile', on_delete=models.CASCADE, null=True, blank=True)

    #role =

    person = ForeignKey(Person, related_name='profile', on_delete=models.CASCADE, null=True, blank=True)

    #created
    #updated


class WorkTask(models.Model):
    subject = CharField(max_length=1000)
    date = DateField(default=datetime.now)
    duration = IntegerField()
    start_task = TimeField()
    end_task = TimeField()
    task_reward = FloatField()
    other_expense_amount = FloatField()
    other_expense_note = CharField(max_length=255)


class WorkSheet(models.Model):
    profile = ForeignKey(Profile, related_name='worksheet', on_delete=models.SET_NULL())
    causa = CharField(max_length=255)

    reward = IntegerField()
    total_expense = FloatField()
    prepaid_expense = FloatField()
    debt = FloatField()

    note = CharField(max_length=1000, null=True, blank=True)

    work_task = ForeignKey(WorkTask, related_name='worksheet', on_delete=models.CASCADE())
