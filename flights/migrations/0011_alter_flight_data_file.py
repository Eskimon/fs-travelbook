# Generated by Django 3.2.5 on 2021-08-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0010_auto_20210728_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='data_file',
            field=models.FileField(upload_to='flights/'),
        ),
    ]