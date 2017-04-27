import json

from django.http.response import HttpResponseForbidden
from django.test import TestCase
from django.urls import reverse

from punchline.core.tests.factories import UserFactory

from .factories import (
    AlbumFactory, ArtistFactory, PunchlineFactory, SongFactory,
)


class AdminViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory(is_staff=True, user_permissions='all')
        cls.songs = [
            SongFactory(has_album=True),
            SongFactory(has_album=False),
        ]
        cls.punchlines = [
            PunchlineFactory(song=cls.songs[0]),
            PunchlineFactory(song=cls.songs[1]),
            PunchlineFactory(has_song=False),
        ]

    def test_punchline_view(self):
        self.client.force_login(self.user)
        url = reverse('admin:music_punchline_changelist')
        response = self.client.get(url)
        self.assertNotIsInstance(response, HttpResponseForbidden)

    def test_song_view(self):
        self.client.force_login(self.user)
        url = reverse('admin:music_song_changelist')
        response = self.client.get(url)
        self.assertNotIsInstance(response, HttpResponseForbidden)


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
            SongFactory(title='foo', has_album=False),
            SongFactory(title='bar', has_album=False),
            SongFactory(title='foo', has_album=False),
            SongFactory(title='bar', has_album=False),
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
        self.assertEqual(len(content['results']), 2)
        self.assertEqual(int(content['results'][0]['id']), self.artists[1].pk)
        self.assertEqual(int(content['results'][1]['id']), self.artists[0].pk)

    def test_artist_autocomplete_with_query(self):
        self.client.force_login(self.user)
        url = reverse('admin:artist-autocomplete')
        response = self.client.get(url, data={'q': 'foo'}, content_type='application/json')
        content = response.json()
        self.assertEqual(len(content['results']), 1)
        self.assertEqual(int(content['results'][0]['id']), self.artists[0].pk)

    def test_album_autocomplete_no_query(self):
        self.client.force_login(self.user)
        url = reverse('admin:album-autocomplete')
        response = self.client.get(url, content_type='application/json')
        content = response.json()
        self.assertEqual(len(content['results']), 2)
        self.assertEqual(int(content['results'][0]['id']), self.albums[1].pk)
        self.assertEqual(int(content['results'][1]['id']), self.albums[0].pk)

    def test_album_autocomplete_with_query(self):
        self.client.force_login(self.user)
        url = reverse('admin:album-autocomplete')
        response = self.client.get(url, data={'q': 'foo'}, content_type='application/json')
        content = response.json()
        self.assertEqual(len(content['results']), 1)
        self.assertEqual(int(content['results'][0]['id']), self.albums[0].pk)

    def test_song_autocomplete_no_query(self):
        self.client.force_login(self.user)
        url = reverse('admin:song-autocomplete')
        response = self.client.get(url, content_type='application/json')
        content = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(content['results']), 4)
        self.assertEqual(int(content['results'][0]['id']), self.songs[3].pk)
        self.assertEqual(int(content['results'][1]['id']), self.songs[1].pk)
        self.assertEqual(int(content['results'][2]['id']), self.songs[2].pk)
        self.assertEqual(int(content['results'][3]['id']), self.songs[0].pk)

    def test_song_autocomplete_with_query(self):
        self.client.force_login(self.user)
        url = reverse('admin:song-autocomplete')
        response = self.client.get(url, data={'q': 'foo'}, content_type='application/json')
        content = response.json()
        self.assertEqual(len(content['results']), 2)
        self.assertEqual(int(content['results'][0]['id']), self.songs[2].pk)
        self.assertEqual(int(content['results'][1]['id']), self.songs[0].pk)

    def test_song_autocomplete_no_query_with_artist(self):
        self.client.force_login(self.user)
        url = reverse('admin:song-autocomplete')
        response = self.client.get(
            url,
            data={
                'forward': json.dumps({'artist': self.artists[0].pk}),
            },
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 200)
        content = response.json()
        self.assertEqual(len(content['results']), 2)
        self.assertEqual(int(content['results'][0]['id']), self.songs[1].pk)
        self.assertEqual(int(content['results'][1]['id']), self.songs[0].pk)

    def test_song_autocomplete_with_query_and_artist(self):
        self.client.force_login(self.user)
        url = reverse('admin:song-autocomplete')
        response = self.client.get(
            url,
            data={
                'q': 'foo',
                'forward': json.dumps({'artist': self.artists[0].pk}),
            },
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 200)
        content = response.json()
        self.assertEqual(len(content['results']), 1)
        self.assertEqual(int(content['results'][0]['id']), self.songs[0].pk)
