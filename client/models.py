from django.db import models
from django.db.models import (CharField, EmailField, ForeignKey, IntegerField, DecimalField,
                              DateTimeField, DateField, TimeField, Sum)

from datetime import *
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    name = CharField(max_length=1000, unique=True, verbose_name=_('name'))
    email = EmailField(verbose_name=_('e-mail'))
    phone_number = CharField(max_length=255, null=True, blank=True, verbose_name=_('phone number'))
    id_number = CharField(max_length=12, null=True, blank=True, verbose_name=_('ID number'))
    vat_number = CharField(max_length=12, null=True, blank=True, verbose_name=_('VAT number'))
    created = DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name=_('created'))
    last_updated = DateTimeField(auto_now=True, null=False, blank=False, verbose_name=_('last updated'))

    debt = DecimalField(null=True, blank=True, max_digits=12, decimal_places=2, verbose_name=_('debt'))

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _('Clients')

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
    client = ForeignKey(Client, on_delete=models.CASCADE, related_name='addresses', null=True, blank=True,
                        verbose_name=_('client'))
    street = CharField(max_length=255, verbose_name=_('street'))
    city = CharField(max_length=100, verbose_name=_('city'))
    post_number = CharField(max_length=5, verbose_name=_('post_number'))
    note = CharField(max_length=1000, verbose_name=_('note'), null=True, blank=True, )

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _('Addresses')


class BankAccount(models.Model):
    client = ForeignKey(Client, on_delete=models.CASCADE, related_name='bankaccounts', null=True, blank=True,
                        verbose_name=_('client'))
    account = CharField(max_length=20, verbose_name=_('account'))
    bank_id = CharField(max_length=4, verbose_name=_('bank_id'))

    class Meta:
        verbose_name = _("Bank Account")
        verbose_name_plural = _('Bank Accounts')


class Person(models.Model):
    client = ForeignKey(Client, on_delete=models.SET_NULL, related_name='persons', null=True,
                        verbose_name=_('client'))
    title = CharField(max_length=255, verbose_name=_('title'), null=True, blank=True, )
    first_name = CharField(max_length=255, verbose_name=_('first name'))
    last_name = CharField(max_length=255, verbose_name=_('last name'))
    email = CharField(max_length=255, verbose_name=_('email'), null=True, blank=True)
    phone_number = CharField(max_length=255, null=True, blank=True, verbose_name=_('phone number'))
    role = CharField(max_length=255, verbose_name=_('role'), null=True, blank=True, )

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _('Persons')


class WorkSheet(models.Model):
    client = ForeignKey(Client, related_name='worksheets', on_delete=models.SET_NULL, null=True,
                        verbose_name=_('client'))
    causa = CharField(max_length=255, verbose_name=_('causa'))

    reward = IntegerField(verbose_name=_('reward'))
    total_reward = DecimalField(null=True, blank=True, max_digits=12, decimal_places=2, verbose_name=_('total reward'))
    total_other_task_expense = DecimalField(null=True, blank=True, max_digits=12, decimal_places=2,
                                            verbose_name=_('total other task expense'))
    total_expense = DecimalField(null=True, blank=True, max_digits=12, decimal_places=2,
                                 verbose_name=_('total expense'))

    note = CharField(max_length=1000, null=True, blank=True, verbose_name=_('note'))

    class Meta:
        verbose_name = _("WorkSheet")
        verbose_name_plural = _('WorkSheets')

    def __str__(self):
        return f"{self.causa} - {self.client}"

    # def clean(self):
    # self.total_reward = round(self.work_tasks.all().aggregate(Sum('task_reward'))['task_reward__sum'], 2)
    # self.total_other_task_expense = round(self.work_tasks.all()
    #                                       .aggregate(Sum('other_expense_amount'))['other_expense_amount__sum'], 2)
    # self.total_expense = self.total_reward + self.total_other_task_expense

    def save(self, *args, **kwargs):
        super(WorkSheet, self).save(*args, **kwargs)

    def calculate_reward(self):
        try:
            self.total_reward = round(self.work_tasks.all().aggregate(Sum('task_reward'))['task_reward__sum'], 2)
        except TypeError:
            self.total_reward = 0
        try:
            self.total_other_task_expense = round(self.work_tasks.all()
                                                  .aggregate(Sum('other_expense_amount'))['other_expense_amount__sum'],
                                                  2)
        except TypeError:
            self.total_other_task_expense = 0
        self.total_expense = self.total_reward + self.total_other_task_expense
        self.save()


class WorkTask(models.Model):
    worksheet = ForeignKey(WorkSheet, on_delete=models.CASCADE, related_name='work_tasks',
                           verbose_name=_('worksheet'))
    subject = CharField(max_length=1000, verbose_name=_('subject'))
    date = DateField(default=datetime.now, verbose_name=_('date'))
    duration = IntegerField(verbose_name=_('duration'), blank=True, null=True)
    start_task = TimeField(null=True, blank=True, verbose_name=_('begin of task'))
    end_task = TimeField(null=True, blank=True, verbose_name=_('end of task'))
    task_reward = DecimalField(null=True, blank=True, max_digits=12, decimal_places=2,
                               verbose_name=_('task reward'))
    other_expense_amount = DecimalField(null=True, blank=True, max_digits=12, decimal_places=2,
                                        verbose_name=_('other expense amount'))
    other_expense_note = CharField(max_length=255, null=True, blank=True, verbose_name=_('other expense note'))

    class Meta:
        verbose_name = _("WorkTask")
        verbose_name_plural = _('WorkTasks')

    def __str__(self):
        return f"{self.subject}, {self.date} ({self.worksheet})"

    def get_task_reward(self):
        task_reward = self.duration * (self.worksheet.reward / 60)
        return round(task_reward, 0)

    def save(self, *args, **kwargs):
        if self.start_task and self.end_task:
            self.duration = (datetime.combine(date.today(), self.end_task) -
                             datetime.combine(date.today(), self.start_task)).seconds / 60
        self.task_reward = self.get_task_reward()
        super(WorkTask, self).save(*args, **kwargs)
        self.worksheet.calculate_reward()


class Payments(models.Model):
    client = ForeignKey(Client, related_name='payments', on_delete=models.SET_NULL, null=True, verbose_name=_('client'))
    date = DateField(verbose_name=_('date'))
    amount = DecimalField(null=False, blank=False, max_digits=12, decimal_places=2, verbose_name=_('amount'))

    class Meta:
        verbose_name = _("Payments")
        verbose_name_plural = _('Payments')

    def __str__(self):
        return f'{self.client} - {self.amount} - {self.date}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.client.save()
