<<<<<<< HEAD
# Generated by Django 4.2 on 2023-05-17 08:48
=======
# Generated by Django 4.2 on 2023-05-17 10:52
>>>>>>> 453197856dcf9523daddc0c81982d5938d3b77fa

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0035_alter_order_delivered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_date',
<<<<<<< HEAD
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 20, 8, 48, 25, 573398, tzinfo=datetime.timezone.utc), editable=False),
=======
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 20, 10, 52, 53, 280494, tzinfo=datetime.timezone.utc), editable=False),
>>>>>>> 453197856dcf9523daddc0c81982d5938d3b77fa
        ),
    ]
