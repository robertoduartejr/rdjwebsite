# Generated by Django 4.1.4 on 2023-01-07 01:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteblog', '0031_visitorspost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateField(default=datetime.date(2023, 1, 6)),
        ),
        migrations.AlterField(
            model_name='visitorspost',
            name='created_at',
            field=models.DateField(default=datetime.date(2023, 1, 6)),
        ),
    ]
