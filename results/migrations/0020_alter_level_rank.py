# Generated by Django 4.0.3 on 2022-05-06 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0019_rename_teacherclassroomsubjects_teacherclassroomsubject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='rank',
            field=models.IntegerField(unique=True),
        ),
    ]
