# Generated by Django 4.0.3 on 2022-05-05 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0018_remove_teacher_class_rooms'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeacherClassRoomSubjects',
            new_name='TeacherClassRoomSubject',
        ),
    ]
