# Generated by Django 3.2.5 on 2021-07-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0008_alter_products_modified_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]