from django.test import TestCase
from django.urls import reverse

from core.tests.factories import UserFactory
from music.tests.factories import (
    AlbumFactory, ArtistFactory, PunchlineFactory, SongFactory,
)


class AdminAutocompleteViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory(is_staff=True)
        cls.artists = [
            ArtistFactory(nickname='foo'),
            ArtistFactory(nickname='bar'),
        ]
        cls.albums = [
            AlbumFactory(name='foo'),
            AlbumFactory(name='bar'),
        ]
        cls.songs = [
            SongFactory(title='foo'),
            SongFactory(title='bar'),
            SongFactory(title='foo'),
            SongFactory(title='bar'),
        ]
        PunchlineFactory(artist=cls.artists[0], song=cls.songs[0])
        PunchlineFactory(artist=cls.artists[0], song=cls.songs[1])
        PunchlineFactory(artist=cls.artists[1], song=cls.songs[2])
        PunchlineFactory(artist=cls.artists[1], song=cls.songs[3])

    def test_artist_autocomplete_no_query(self):
        self.client.force_login(self.user)
        url = reverse('admin:artist-autocomplete')
        response = self.client.get(url, content_type='application/json')
        content = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(content), 2)
        self.assertEqual(content['results'][0]['id'], self.artists[1].pk)
        self.assertEqual(content['results'][1]['id'], self.artists[0].pk)

    def test_artist_autocomplete_with_query(self):
        self.client.force_login(self.user)
        url = reverse('admin:artist-autocomplete')
        response = self.client.get(url, data={'q': 'foo'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data['results'][0]['id'], self.artists[1].pk)

    def test_album_autocomplete_no_query(self):
        self.client.force_login(self.user)
        url = reverse('admin:album-autocomplete')
        response = self.client.get(url)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data['results'][0]['id'], self.albums[1].pk)
        self.assertEqual(response.data['results'][1]['id'], self.albums[0].pk)

    def test_album_autocomplete_with_query(self):
        self.client.force_login(self.user)
        url = reverse('admin:album-autocomplete')
        response = self.client.get(url, data={'q': 'foo'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data['results'][0]['id'], self.albums[1].pk)

    def test_song_autocomplete_no_query(self):
        self.client.force_login(self.user)
        url = reverse('admin:song-autocomplete')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data['results'][0]['id'], self.songs[3].pk)
        self.assertEqual(response.data['results'][1]['id'], self.songs[1].pk)
        self.assertEqual(response.data['results'][2]['id'], self.songs[2].pk)
        self.assertEqual(response.data['results'][3]['id'], self.songs[0].pk)

    def test_song_autocomplete_with_query(self):
        self.client.force_login(self.user)
        url = reverse('admin:song-autocomplete')
        response = self.client.get(url, data={'q': 'foo'})
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data['results'][0]['id'], self.songs[3].pk)
        self.assertEqual(response.data['results'][1]['id'], self.songs[1].pk)

    def test_song_autocomplete_no_query_with_artist(self):
        self.client.force_login(self.user)
        url = reverse('admin:song-autocomplete')
        response = self.client.get(url, data={'forward': 'artist='.format(self.artists[0])})
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data['results'][0]['id'], self.songs[1].pk)
        self.assertEqual(response.data['results'][1]['id'], self.songs[0].pk)

    def test_song_autocomplete_with_query_and_artist(self):
        self.client.force_login(self.user)
        url = reverse('admin:song-autocomplete')
        response = self.client.get(url, data={
            'q': 'foo',
            'forward': 'artist='.format(self.artists[0]),
        })
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data['results'][0]['id'], self.songs[0].pk)
