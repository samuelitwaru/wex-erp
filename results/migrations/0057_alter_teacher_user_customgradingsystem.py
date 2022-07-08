# Generated by Django 4.0.3 on 2022-07-07 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('results', '0056_activity_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CustomGradingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('class_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.classroom')),
                ('grading_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.gradingsystem')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.subject')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]