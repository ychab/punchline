from django.contrib import admin

from .models import Album, Artist, Song


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_select_related = ('author',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'album')
    list_select_related = ('album',)
