# Generated by Django 4.0.3 on 2022-08-07 03:11

import core.models
from django.db import migrations
import django_resized.forms
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='signature',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=-1, size=[200, 200], storage=utils.OverwiteStorageSystem, upload_to=core.models.user_signature_upload_location),
        ),
    ]
