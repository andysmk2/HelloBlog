from django.contrib import admin
from django.contrib.auth.models import User
import models

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'email', 'date')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('user','cell_phone',)

admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.Client, ClientAdmin)