# Generated by Django 4.0.3 on 2022-05-31 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0021_alter_assessment_options_alter_paper_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='initials',
            field=models.CharField(default='IS', max_length=8),
            preserve_default=False,
        ),
    ]