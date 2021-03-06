from datetime import timedelta

from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import get_language, to_locale

import factory
from factory import fuzzy

from punchline.core.tests.factories import (
    AuthorFactory, PunchlineFactory as BasePunchlineFactory,
)

from ..models import Album, Artist, Punchline, Song

language = get_language() or 'en-us'
locale = to_locale(language)


class ArtistFactory(AuthorFactory):
    class Meta:
        model = Artist

    nickname = factory.Faker('name', locale=locale)
    slug = factory.LazyAttribute(lambda o: slugify(o.nickname))


class AlbumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Album

    name = factory.Faker('sentence', locale=locale)
    slug = factory.LazyAttribute(lambda o: slugify(o.name))
    date = fuzzy.FuzzyDateTime(start_dt=timezone.now() - timedelta(days=365*10))


class SongFactory(factory.DjangoModelFactory):
    class Meta:
        model = Song

    title = factory.Faker('sentence', locale=locale)
    slug = factory.LazyAttribute(lambda o: slugify(o.title))
    date = fuzzy.FuzzyDateTime(start_dt=timezone.now() - timedelta(days=365*10))
    has_album = True

    class Params:
        has_album = factory.Trait(
            album=factory.SubFactory(AlbumFactory)
        )


class PunchlineFactory(BasePunchlineFactory):
    class Meta:
        model = Punchline

    artist = factory.SubFactory(ArtistFactory)
    has_song = True

    class Params:
        has_song = factory.Trait(
            song=factory.SubFactory(SongFactory)
        )
