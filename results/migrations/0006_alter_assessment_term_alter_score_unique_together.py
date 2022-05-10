# Generated by Django 4.0.3 on 2022-04-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_assessment_teacher_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='term',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together={('assessment', 'student')},
        ),
    ]
