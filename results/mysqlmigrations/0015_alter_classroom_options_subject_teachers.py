# Generated by Django 4.0.3 on 2022-05-05 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0014_gradingsystem_is_default_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={'ordering': ('level',)},
        ),
        migrations.AddField(
            model_name='subject',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='subjects', to='results.teacher'),
        ),
    ]
