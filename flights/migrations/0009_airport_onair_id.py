# Generated by Django 3.2.5 on 2021-07-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0008_auto_20210722_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='onair_id',
            field=models.CharField(blank=True, max_length=36, null=True, unique=True),
        ),
    ]
