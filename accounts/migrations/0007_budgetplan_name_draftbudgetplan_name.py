# Generated by Django 4.0.3 on 2022-04-30 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_accountsjournals_siblings'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetplan',
            name='name',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='draftbudgetplan',
            name='name',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
