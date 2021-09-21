from django.contrib import admin
from main import models

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','full_name', 'email', 'phone')
    list_display_links = ('id','user','full_name', 'email', 'phone')
    search_fields = ('id','full_name')
    list_per_page = 20

admin.site.register(models.Profile, ProfileAdmin)