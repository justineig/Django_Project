from django.contrib import admin
from Bands.models import Musicians

@admin.register(Musicians)
class MusicianAdmin(admin.ModelAdmin):
    pass


