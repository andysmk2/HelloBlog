from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=20)

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
    title = models.CharField(max_length = 50)
    subtitle = models.CharField(max_length = 50, blank = True)
    menu = models.ForeignKey(Menu, default = 1)

    def __unicode__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField(max_length = 500)
    editor = models.ForeignKey(Editor, default = 1)
    category = models.ForeignKey(Category, default = 1)
    page = models.ForeignKey(Page, default = 1)
    # picture = models
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title



