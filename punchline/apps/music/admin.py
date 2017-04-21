from django.contrib import admin

from polymorphic.admin import PolymorphicChildModelAdmin

from .models import Album, Artist, Song


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(Artist)
class ArtistAdmin(PolymorphicChildModelAdmin):
    base_model = Artist

    list_display = ('id',)


@admin.register(Song)
class SongAdmin(PolymorphicChildModelAdmin):
    base_model = Song

    list_display = ('id', 'title', 'album')
    list_select_related = ('album',)
