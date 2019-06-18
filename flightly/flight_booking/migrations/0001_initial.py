# Generated by Django 2.2.2 on 2019-06-17 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import flightly.flight_booking.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Flight Name')),
                ('departure_airport', models.CharField(max_length=50, verbose_name='Departure Airport')),
                ('arrival_airport', models.CharField(max_length=50, verbose_name='Arrival Airport')),
                ('departure_datetime', models.DateTimeField(verbose_name='Departure Time')),
                ('capacity', models.IntegerField(verbose_name='Carrying Capacity')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Ticket Price')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ticket_number', models.CharField(default=flightly.flight_booking.models.Reservation.generate_ticket_number, max_length=23, unique=True)),
                ('status', models.CharField(choices=[('unpaid', 'Unpaid'), ('paid', 'Paid'), ('cancelled', 'Cancelled')], default='unpaid', max_length=10)),
                ('flight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flight_booking.Flight')),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]