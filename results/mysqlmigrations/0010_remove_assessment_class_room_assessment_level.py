# Generated by Django 4.0.3 on 2022-04-24 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0009_remove_classroom_subjects_remove_subject_levels_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessment',
            name='class_room',
        ),
        migrations.AddField(
            model_name='assessment',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.level'),
        ),
    ]
