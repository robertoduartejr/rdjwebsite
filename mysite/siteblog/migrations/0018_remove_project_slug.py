# Generated by Django 4.1.4 on 2022-12-21 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteblog', '0017_alter_project_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='slug',
        ),
    ]