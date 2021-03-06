# Generated by Django 3.2.5 on 2021-07-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_category', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('product_image', models.CharField(max_length=800)),
                ('product_stock', models.BooleanField()),
                ('product_price', models.FloatField()),
                ('sale_price', models.FloatField()),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('modified_date', models.DateTimeField()),
            ],
        ),
    ]
