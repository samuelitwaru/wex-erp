# Generated by Django 4.0.3 on 2022-06-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0047_report_a_result_report_o_result_report_p_result_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]