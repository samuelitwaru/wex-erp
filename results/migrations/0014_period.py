# Generated by Django 4.0.3 on 2022-05-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0013_teacher_picture_alter_student_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('start', models.DateField()),
                ('stop', models.DateField()),
            ],
        ),
    ]
