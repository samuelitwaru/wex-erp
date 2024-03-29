# Generated by Django 4.0.3 on 2022-07-21 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_remove_period_promotions_opened'),
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
