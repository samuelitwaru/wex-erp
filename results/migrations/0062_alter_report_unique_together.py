# Generated by Django 4.0.3 on 2022-07-08 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0061_activity_is_open'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='report',
            unique_together={('student', 'period', 'level')},
        ),
    ]
