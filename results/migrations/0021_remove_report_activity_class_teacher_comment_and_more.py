# Generated by Django 4.0.3 on 2022-08-25 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0020_report_competency_class_teacher_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='activity_class_teacher_comment',
        ),
        migrations.RemoveField(
            model_name='report',
            name='activity_head_teacher_comment',
        ),
    ]
