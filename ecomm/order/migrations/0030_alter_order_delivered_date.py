# Generated by Django 4.2 on 2023-05-16 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0029_alter_order_delivered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 19, 29, 5, 741184, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
