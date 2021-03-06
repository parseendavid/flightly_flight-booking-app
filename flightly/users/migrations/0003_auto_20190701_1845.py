# Generated by Django 2.2.2 on 2019-07-01 18:45

from django.db import migrations, models
import flightly.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_flightlyuser_photograph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightlyuser',
            name='photograph',
            field=models.ImageField(default='img/default_user_photo.png',
                                    upload_to=flightly.users.models.user_directory_path, verbose_name='Passport Photograph'),
        ),
    ]
