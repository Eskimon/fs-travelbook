# Generated by Django 3.2.5 on 2021-08-09 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0012_flight_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='intended',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intended', to='flights.airport'),
        ),
    ]
