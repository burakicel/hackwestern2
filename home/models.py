from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Tutorial(models.Model):
    user = models.ForeignKey(User)
    tutorial_title = models.CharField(max_length=200)
    repo_link = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    def __str__(self):              # __unicode__ on Python 2
        return self.tutorial_title


# Create your models here.
