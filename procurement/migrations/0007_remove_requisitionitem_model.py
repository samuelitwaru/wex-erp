# Generated by Django 4.0.3 on 2022-04-16 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0006_vendor_requisition_delivery_date_max_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisitionitem',
            name='model',
        ),
    ]