# Generated by Django 3.2.5 on 2021-07-08 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0010_auto_20210708_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_views',
            old_name='product_id',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='product_views',
            old_name='viewers_list',
            new_name='views_list',
        ),
    ]
