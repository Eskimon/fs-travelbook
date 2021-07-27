# Generated by Django 3.2.5 on 2021-07-26 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0008_auto_20210722_1436'),
        ('pictures', '0002_alter_picture_data_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='flight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pictures', to='flights.flight'),
        ),
    ]