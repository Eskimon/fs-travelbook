# Generated by Django 3.2.5 on 2021-08-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_alter_myuser_icons'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='maps',
            field=models.PositiveIntegerField(choices=[(0, 'None'), (1, 'Icons'), (2, 'Circle')], default=0),
        ),
    ]
