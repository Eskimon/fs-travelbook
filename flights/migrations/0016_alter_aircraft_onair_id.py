# Generated by Django 3.2.5 on 2021-08-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0015_auto_20210810_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='onair_id',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
