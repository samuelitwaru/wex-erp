# Generated by Django 4.0.3 on 2022-04-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_accountingsettings_item_alter_accounttype_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subaccount',
            name='closing_balance',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
