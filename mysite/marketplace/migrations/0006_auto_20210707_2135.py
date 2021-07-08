# Generated by Django 3.2.5 on 2021-07-07 16:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0005_auto_20210707_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='products',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
