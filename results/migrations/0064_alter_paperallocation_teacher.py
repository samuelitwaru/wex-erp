# Generated by Django 4.0.3 on 2022-07-08 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0063_rename_teacherclassroompaper_paperallocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperallocation',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.teacher'),
        ),
    ]