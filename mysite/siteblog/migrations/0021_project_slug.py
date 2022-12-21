# Generated by Django 4.1.4 on 2022-12-21 04:10

from django.db import migrations, models
from ..models import Project

def migrate_data_forward(apps, schema_editor):
    for instance in Project.objects.all():
        print(f"Generating slug for {instance}")
        instance.save() # Will trigger slug update

def migrate_data_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):


    dependencies = [
        ('siteblog', '0020_remove_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=None, max_length=100, null=True, unique=True),
        ),
    ]
