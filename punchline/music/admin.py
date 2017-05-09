from django.contrib import admin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .forms import PunchlineAdminForm, SongAdminForm
from .models import Album, Artist, Punchline, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('nickname',)
    search_fields = ('nickname',)
    list_per_page = 50

    fields = (
        ('nickname', 'slug'),
        ('first_name', 'last_name', 'birth_date',),
        ('description', 'image'),
    )
    prepopulated_fields = {
        'slug': ('nickname',),
    }


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('name',)
    ordering = ('-date',)
    list_per_page = 50

    fields = ('name', 'slug', 'date')
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album_link', 'date')
    list_select_related = ('album',)
    search_fields = ('title', 'album__name')
    ordering = ('-date',)
    list_per_page = 50

    form = SongAdminForm
    fields = ('title', 'slug', 'album', 'date')
    prepopulated_fields = {
        'slug': ('title',),
    }

    def album_link(self, obj):
        if obj.album:
            return '<a href="{href}" target="_blank">{album}</a>'.format(
                href=reverse('admin:music_album_change', args=(obj.album.pk,)),
                album=obj.album,
            )
    album_link.allow_tags = True
    album_link.short_description = _('Album')
    album_link.admin_order_field = 'album__name'


@admin.register(Punchline)
class PunchlineAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'artist_link', 'teaser', 'album_link', 'song_link', 'created',
        'modified',
    )
    list_select_related = ('artist', 'song__album')
    search_fields = (
        'text', 'artist__nickname', 'song__title', 'song__album__name',
    )
    ordering = ('-modified',)
    list_per_page = 50

    form = PunchlineAdminForm
    fields = ('artist', 'text', 'song')

    def artist_link(self, obj):
        return '<a href="{href}" target="_blank">{artist}</a>'.format(
            href=reverse('admin:music_artist_change', args=(obj.artist.pk,)),
            artist=obj.artist,
        )
    artist_link.allow_tags = True
    artist_link.short_description = _('Artist')
    artist_link.admin_order_field = 'artist__nickname'

    def album_link(self, obj):
        if obj.song and obj.song.album:
            return '<a href="{href}" target="_blank">{album}</a>'.format(
                href=reverse('admin:music_album_change', args=(obj.song.album.pk,)),
                album=obj.song.album,
            )
    album_link.allow_tags = True
    album_link.short_description = _('Album')
    album_link.admin_order_field = 'song__album__name'

    def song_link(self, obj):
        if obj.song:
            return '<a href="{href}" target="_blank">{song}</a>'.format(
                href=reverse('admin:music_song_change', args=(obj.song.pk,)),
                song=obj.song,
            )
    song_link.allow_tags = True
    song_link.short_description = _('Song')
    song_link.admin_order_field = 'song__title'
