# Generated by Django 4.0.3 on 2022-04-17 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0008_rename_comments_requisition_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('metric', models.CharField(max_length=128)),
                ('request_for_quotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procurement.requestforquotation')),
                ('requisition_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procurement.requisitionitem')),
            ],
        ),
    ]
