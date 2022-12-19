# Generated by Django 4.1.4 on 2022-12-19 14:49

import ckeditor.fields
from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('siteblog', '0005_project_content_project_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='learning',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='programming_languages',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
