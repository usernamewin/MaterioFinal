from django.contrib import admin

# Register your models here.
from .models import Album, Song, Award, Artist

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Award)
admin.site.register(Artist)