# Generated by Django 4.2 on 2023-05-05 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
