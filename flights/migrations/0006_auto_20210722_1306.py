# Generated by Django 3.2.5 on 2021-07-22 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flights', '0005_auto_20210722_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='flight',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waypoints', to='flights.flight'),
        ),
    ]
