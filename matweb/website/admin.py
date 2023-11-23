from django.contrib import admin
from . import models
# Register your models here.
class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(models.Image, imageAdmin)