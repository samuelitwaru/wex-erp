# Generated by Django 4.0.3 on 2022-06-12 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0031_level_level_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='levelgroup',
            name='full',
            field=models.CharField(default='Ordinary', max_length=128),
            preserve_default=False,
        ),
    ]