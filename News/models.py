from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length = 20)
    disc = models.CharField(max_length = 100, blank = True)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(max_length = 50)
    subtitle = models.CharField(max_length = 50, blank = True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField(max_length = 500)
    author = models.ForeignKey(Author)
    category = models.ManyToManyField(Category)
    # picture = models
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title



