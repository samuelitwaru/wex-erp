# Generated by Django 4.0.3 on 2022-07-14 08:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField(unique=True)),
                ('_additional_data', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountsJournals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('amount', models.BigIntegerField()),
                ('item_id', models.TextField()),
                ('entry_type', models.TextField(choices=[('DEBIT', 'Debit'), ('CREDIT', 'Credit')])),
                ('_additional_data', models.TextField()),
                ('siblings', models.ManyToManyField(to='accounts.accountsjournals')),
            ],
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, unique=True)),
                ('increase', models.TextField(choices=[('DEBIT', 'Debit'), ('CREDIT', 'Credit')])),
                ('_additional_data', models.TextField(blank=True)),
                ('state', models.TextField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='AccountTypeSubAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('account_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.accounttype')),
            ],
        ),
        migrations.CreateModel(
            name='BudgetPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('identifier', models.TextField(db_index=True, unique=True)),
                ('name', models.TextField(db_index=True)),
                ('amount', models.IntegerField()),
                ('_additional_data', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('contacts', models.TextField()),
                ('_additional_data', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DraftBudgetPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('identifier', models.TextField(db_index=True, unique=True)),
                ('name', models.TextField(db_index=True)),
                ('amount', models.IntegerField()),
                ('_additional_data', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FiscalYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(db_index=True, unique=True)),
                ('end', models.DateField(db_index=True, unique=True)),
                ('state', models.TextField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN')),
            ],
        ),
        migrations.CreateModel(
            name='SubAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, unique=True)),
                ('opening_balance', models.BigIntegerField()),
                ('closing_balance', models.BigIntegerField(blank=True, null=True)),
                ('state', models.TextField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('_additional_data', models.TextField(blank=True)),
                ('account_type', models.ManyToManyField(through='accounts.AccountTypeSubAccount', to='accounts.accounttype')),
            ],
        ),
        migrations.CreateModel(
            name='SubAccountAccountsJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('accounts_journal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.accountsjournals')),
                ('sub_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.subaccount')),
            ],
        ),
        migrations.CreateModel(
            name='FiscalYearBudgetPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.budgetplan')),
                ('fiscal_year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.fiscalyear')),
            ],
        ),
        migrations.CreateModel(
            name='FiscalYearAccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('account_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.accounttype')),
                ('fiscal_year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.fiscalyear')),
            ],
        ),
        migrations.AddField(
            model_name='fiscalyear',
            name='account_types',
            field=models.ManyToManyField(through='accounts.FiscalYearAccountType', to='accounts.accounttype'),
        ),
        migrations.AddField(
            model_name='budgetplan',
            name='fiscalYear',
            field=models.ManyToManyField(through='accounts.FiscalYearBudgetPlan', to='accounts.fiscalyear'),
        ),
        migrations.AddField(
            model_name='accounttypesubaccount',
            name='sub_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.subaccount'),
        ),
        migrations.AddField(
            model_name='accountsjournals',
            name='sub_account',
            field=models.ManyToManyField(through='accounts.SubAccountAccountsJournal', to='accounts.subaccount'),
        ),
    ]
