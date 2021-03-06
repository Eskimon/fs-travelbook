# Generated by Django 3.2.5 on 2021-07-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0003_alter_picture_flight'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='picture',
            name='lon',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
