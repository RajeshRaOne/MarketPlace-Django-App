# Generated by Django 3.2.5 on 2021-07-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0009_alter_products_modified_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('friends_list', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='product_views',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('viewers_list', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.IntegerField(unique=True),
        ),
    ]