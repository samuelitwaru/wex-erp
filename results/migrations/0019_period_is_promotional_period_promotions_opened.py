# Generated by Django 4.0.3 on 2022-08-16 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0018_remove_period_is_promotional_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='is_promotional',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='period',
            name='promotions_opened',
            field=models.BooleanField(default=False),
        ),
    ]
