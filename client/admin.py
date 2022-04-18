from django.contrib.admin import site
from django.contrib.admin import TabularInline, ModelAdmin
from .models import Person, Profile, Address, WorkSheet, WorkTask, BankAccount, Payments

from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin, ImportMixin

class WorkSheetResource(resources.ModelResource):

    class Meta:
        model = WorkSheet
        fields = ('__all__')

class AddressTabularInlineAdmin(TabularInline):
    model = Address
    extra = 0
    fields = ('street', 'city', 'post_number', 'note')


class BankAccountTabularInlineAdmin(TabularInline):
    model = BankAccount
    extra = 0
    fields = ('account', 'bank_id',)


class PersonTabularInlineAdmin(TabularInline):
    model = Person
    extra = 0
    fields = ('title', 'first_name', 'last_name', 'role', )


class ProfileAdmin(ModelAdmin):
    list_display = ('name', 'email', 'debt')
    fields = ('name', 'email', 'phone_number', 'id_number', 'vat_number', 'debt',)
    inlines = (AddressTabularInlineAdmin, BankAccountTabularInlineAdmin, PersonTabularInlineAdmin)


class WorkTaskInlineAdmin(TabularInline):
    model = WorkTask
    fields = ('subject', 'date', 'duration', 'start_task', 'end_task', 'task_reward',
              'other_expense_note', 'other_expense_amount')
    extra = 0


class WorkSheetAdmin(ImportExportModelAdmin, ImportMixin):
    fields = ('profile', 'causa', 'reward', 'total_reward', 'total_other_task_expense', 'total_expense', 'note',)
    inlines = (WorkTaskInlineAdmin,)
    resources = WorkSheetResource

    change_list_template = 'admin/import_export/change_list_import.html'
    import_template_name = 'admin/import_export/import.html'


class PaymentsAdmin(ModelAdmin):
    model = Payments
    fields = ('profile', 'amount', 'date')
    list_display = ('profile', 'amount', 'date')


site.register(Profile, ProfileAdmin)
site.register(WorkSheet, WorkSheetAdmin)
site.register(Payments, PaymentsAdmin)
