from django.contrib import admin

# Register your models here.

from .models import Bookmark

class AdminBookmark(admin.ModelAdmin):
    list_display = ['id', 'site_name', 'url']


admin.site.register(Bookmark, AdminBookmark)