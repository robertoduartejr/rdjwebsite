from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

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
    programming_languages = TaggableManager()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)