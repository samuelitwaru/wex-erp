# Generated by Django 4.0.3 on 2022-05-14 04:25

from django.db import migrations, models
import results.models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0012_student_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='picture',
            field=models.ImageField(blank=True, null=True, storage=utils.OverwiteStorageSystem, upload_to=results.models.teacher_picture_upload_loacation),
        ),
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, null=True, storage=utils.OverwiteStorageSystem, upload_to=results.models.student_picture_upload_loacation),
        ),
    ]
