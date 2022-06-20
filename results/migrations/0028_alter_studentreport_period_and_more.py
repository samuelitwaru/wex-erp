# Generated by Django 4.0.3 on 2022-06-11 09:07

from django.db import migrations, models
import django.db.models.deletion
import results.models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0027_studentreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreport',
            name='period',
            field=models.ForeignKey(default=results.models.period_default, on_delete=django.db.models.deletion.CASCADE, to='results.period'),
        ),
        migrations.AlterField(
            model_name='studentreport',
            name='student',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='results.student'),
            preserve_default=False,
        ),
    ]