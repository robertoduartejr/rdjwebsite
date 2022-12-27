# Generated by Django 4.1.4 on 2022-12-26 16:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteblog', '0026_visitorspost'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitorspost',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='siteblog.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateField(default=datetime.date(2022, 12, 26)),
        ),
    ]