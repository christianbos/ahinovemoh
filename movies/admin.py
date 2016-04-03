from django.contrib import admin
from .models import Movies


class MoviesAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'cine', 'horario']

admin.site.register(Movies, MoviesAdmin)
