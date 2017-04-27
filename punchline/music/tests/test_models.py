from django.test import TestCase

from ..models import Punchline
from .factories import (
    AlbumFactory, ArtistFactory, PunchlineFactory, SongFactory,
)


class RelationshipTestCase(TestCase):

    def test_delete_album(self):
        album = AlbumFactory()
        song = SongFactory(album=album)
        album.delete()
        song.refresh_from_db()
        self.assertTrue(song.pk)

    def test_delete_song(self):
        song = SongFactory()
        punchline = PunchlineFactory(song=song)
        song.delete()
        punchline.refresh_from_db()
        self.assertTrue(punchline.pk)

    def test_delete_artist(self):
        artist = ArtistFactory()
        album = AlbumFactory()
        song = SongFactory(album=album)
        punchline = PunchlineFactory(artist=artist, song=song)

        artist.delete()
        with self.assertRaises(Punchline.DoesNotExist):
            punchline.refresh_from_db()

        song.refresh_from_db()
        self.assertTrue(song.pk)
        album.refresh_from_db()
        self.assertTrue(album.pk)
