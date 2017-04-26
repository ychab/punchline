from django.conf.urls import url
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User

from music.admin import (
    AlbumAdmin, ArtistAdmin, PunchlineAdmin, SongAdmin,
)
from music.models import Album, Artist, Punchline, Song
from music.views import (
    AlbumAutocompleteView, ArtistAutocompleteView, SongAutocompleteView,
)


class PunchlineAdminSite(AdminSite):

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            url(
                r'^artist-autocomplete/$',
                self.admin_view(ArtistAutocompleteView.as_view(create_field='nickname')),
                name='artist-autocomplete',
            ),
            url(
                r'^album-autocomplete/$',
                self.admin_view(AlbumAutocompleteView.as_view(create_field='name')),
                name='album-autocomplete',
            ),
            url(
                r'^song-autocomplete/$',
                self.admin_view(SongAutocompleteView.as_view(create_field='title')),
                name='song-autocomplete',
            ),
        ]
        return urls


site = PunchlineAdminSite()

site.register(Group, GroupAdmin)
site.register(User, UserAdmin)

site.register(Artist, ArtistAdmin)
site.register(Album, AlbumAdmin)
site.register(Song, SongAdmin)
site.register(Punchline, PunchlineAdmin)
