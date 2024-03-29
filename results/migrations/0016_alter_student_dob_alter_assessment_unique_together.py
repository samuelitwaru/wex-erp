# Generated by Django 4.0.3 on 2022-08-01 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0015_assessment_assessment_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='assessment',
            unique_together={('paper', 'class_room', 'assessment_category')},
        ),
    ]
