from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.utils.translation import get_language, to_locale

import factory
from factory import fuzzy

language = get_language() or 'en-us'
locale = to_locale(language)


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: 'user_%d' % n)
    password = factory.PostGenerationMethodCall('set_password', 'test')
    email = factory.LazyAttribute(lambda o: '%s@example.com' % o.username)

    @factory.post_generation
    def user_permissions(self, create, extracted, **kwargs):
        if create and extracted:
            if extracted == 'all':
                self.user_permissions.set(UserFactory.get_permissions())
            else:
                self.user_permissions.set(
                    Permission.objects.filter(codename__in=extracted))

    @classmethod
    def get_permissions(cls):
        if not hasattr(cls, '_permissions'):
            cls._permissions = Permission.objects.filter(
                content_type__in=ContentType.objects.filter(
                    app_label__in=(
                        'core',
                        'music',
                    ),
                ),
            )
        return cls._permissions


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
