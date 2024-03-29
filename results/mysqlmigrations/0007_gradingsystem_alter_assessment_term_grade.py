# Generated by Django 4.0.3 on 2022-04-24 03:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0006_alter_assessment_term_alter_score_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.AlterField(
            model_name='assessment',
            name='term',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
                ('min_mark', models.DecimalField(decimal_places=0, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('max_mark', models.DecimalField(decimal_places=0, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('points', models.IntegerField(null=True)),
                ('aggregates', models.IntegerField(null=True)),
                ('grading_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.gradingsystem')),
            ],
            options={
                'unique_together': {('grading_system', 'min_mark', 'max_mark', 'category')},
            },
        ),
    ]
