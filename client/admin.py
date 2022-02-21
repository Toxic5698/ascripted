from django.contrib.admin import site
from django.contrib.admin import TabularInline, ModelAdmin
from .models import Person, Profile, Address, WorkSheet, WorkTask, BankAccount


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
    fields = ('name', 'email', 'phone_number', 'id_number', 'vat_number', )
    inlines = (AddressTabularInlineAdmin, BankAccountTabularInlineAdmin, PersonTabularInlineAdmin)


class WorkTaskInlineAdmin(TabularInline):
    model = WorkTask
    fields = ('subject', 'date', 'duration', 'start_task', 'end_task', 'task_reward',
              'other_expense_note', 'other_expense_amount')
    extra = 1


class WorkSheetAdmin(ModelAdmin):
    fields = ('profile', 'causa', 'reward', 'total_expense',
              'prepaid_expense', 'debt', 'note',)
    inlines = (WorkTaskInlineAdmin,)


# site.register(Person, PersonAdmin)
site.register(Profile, ProfileAdmin)
# site.register(Address, AddressAdmin)
site.register(WorkSheet, WorkSheetAdmin)
# site.register(WorkTask, WorkTaskAdmin)
# site.register(BankNumber, BankNumberAdmin)
