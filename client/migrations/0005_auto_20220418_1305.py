# Generated by Django 3.2.9 on 2022-04-18 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20220418_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worksheet',
            name='debt',
        ),
        migrations.RemoveField(
            model_name='worksheet',
            name='prepaid_expense',
        ),
        migrations.AddField(
            model_name='profile',
            name='debt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='prepaid_expense',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='client.profile'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bankaccounts', to='client.profile'),
        ),
        migrations.AlterField(
            model_name='person',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='persons', to='client.profile'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worksheets', to='client.profile'),
        ),
        migrations.AlterField(
            model_name='worktask',
            name='worksheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worktasks', to='client.worksheet'),
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('amount', models.FloatField()),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to='client.profile')),
            ],
        ),
    ]