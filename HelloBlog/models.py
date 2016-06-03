# -​*- coding: UTF-8 -*​-

from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 255)
    content = models.TextField()
    date = models.DateTimeField()


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cell_phone_regex = RegexValidator(regex='^09\d{2}-?\d{3}-?\d{3}$', message='格式錯誤')
    cell_phone = models.CharField(validators=[cell_phone_regex], max_length=13, blank=True)
