from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from datetime import date
from django_extensions.db.fields import AutoSlugField
from django.conf import settings

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField()
    content = RichTextUploadingField()
    learning = RichTextField()
    author = models.ForeignKey(User,on_delete=models.PROTECT)
    repository = models.URLField()
    deploy = models.URLField()
    cover = models.ImageField()
    tags = TaggableManager()
    slug = AutoSlugField(null=True,unique=True, max_length=100,default=None,populate_from='title')
    created_at = models.DateField(default=date.today())

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)

class VisitorsPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField('Deixe um comentário',max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    created_at = models.DateField(default=date.today())

    class Meta:
        ordering = ('-created_at',)
