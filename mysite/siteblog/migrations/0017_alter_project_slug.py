# Generated by Django 4.1.4 on 2022-12-21 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteblog', '0016_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
