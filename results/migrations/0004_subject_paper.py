# Generated by Django 4.0.3 on 2022-05-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_delete_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='paper',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
