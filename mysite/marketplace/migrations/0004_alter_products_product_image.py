# Generated by Django 3.2.5 on 2021-07-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_auto_20210707_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.CharField(default='https://nayemdevs.com/wp-content/uploads/2020/03/default-product-image.png', max_length=800),
        ),
    ]
