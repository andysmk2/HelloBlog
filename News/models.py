from __future__ import unicode_literals
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.name


class Editor(models.Model):
    name = models.CharField(max_length = 20)
    disc = models.CharField(max_length = 100, blank = True)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(max_length = 100)
    subtitle = models.CharField(max_length = 100, blank = True)
    menu = models.ForeignKey(Menu, default = 1)

    def __unicode__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, allow_unicode = True)
    content = models.TextField()
    editor = models.ForeignKey(Editor, default = 1)
    category = models.ForeignKey(Category, default = 1)
    page = models.ForeignKey(Page, default = 1)
    date = models.DateTimeField()

    @permalink
    def get_absolute_url(self):
        return reverse('single_article',args = {'slug': self.slug})

    def __unicode__(self):
        return self.title



class Contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 255)
    content = models.TextField()
    date = models.DateTimeField()

