# Generated by Django 4.0.3 on 2022-04-23 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(related_name='students', to='results.subject'),
        ),
        migrations.AddField(
            model_name='subject',
            name='levels',
            field=models.ManyToManyField(related_name='subjects', to='results.level'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(related_name='teachers', to='results.subject'),
        ),
    ]
