from django.contrib import admin
import models
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'editor', 'thumbnail', 'page', 'category', 'date')
    prepopulated_fields = {"slug": ("title",)}

# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'content', 'email', 'date')

admin.site.register(models.Category)
admin.site.register(models.Page)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Editor)
admin.site.register(models.Menu)
# admin.site.register(models.Contact, ContactAdmin)
