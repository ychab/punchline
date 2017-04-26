from datetime import timedelta

from django.utils import timezone
from django.utils.translation import get_language, to_locale

import factory
from factory import fuzzy

language = get_language() or 'en-us'
locale = to_locale(language)


class AuthorFactory(factory.DjangoModelFactory):
    class Meta:
        abstract = True

    first_name = factory.Faker('first_name', locale=locale)
    last_name = factory.Faker('last_name', locale=locale)

    birth_date = fuzzy.FuzzyDateTime(
        start_dt=timezone.now() - timedelta(days=365*50),
        end_dt=timezone.now() - timedelta(days=365*15),
    )
    description = factory.Faker('text', locale=locale)
    image = factory.django.ImageField()


class PunchlineFactory(factory.DjangoModelFactory):
    class Meta:
        abstract = True

    text = factory.Faker('text', locale=locale)
