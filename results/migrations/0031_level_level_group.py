# Generated by Django 4.0.3 on 2022-06-11 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0030_levelgroup_remove_level_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='level_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='results.levelgroup'),
            preserve_default=False,
        ),
    ]