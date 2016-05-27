from django.contrib import admin
import models
# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Page)
admin.site.register(models.Article)
admin.site.register(models.Author)

