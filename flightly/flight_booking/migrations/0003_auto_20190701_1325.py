# Generated by Django 2.2.2 on 2019-07-01 13:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_booking', '0002_auto_20190701_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='capacity',
            field=models.PositiveIntegerField(verbose_name='Carrying Capacity'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Ticket Price'),
        ),
    ]
