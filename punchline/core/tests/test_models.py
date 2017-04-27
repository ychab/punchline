from django.test import TestCase, override_settings

from .dummy.models import DummyPunchline


@override_settings(LANGUAGE_CODE='en-us')
class BasePunchlineTestCase(TestCase):

    def test_save_language_update(self):
        """
        Only set a default language on update.
        You could change it, even set it to empty string.
        """
        dummy = DummyPunchline.objects.create()
        dummy.language = ''
        dummy.save()
        dummy.refresh_from_db()
        self.assertEqual(dummy.language, '')

    def test_save_language_set(self):
        dummy = DummyPunchline.objects.create(language='fr_FR')
        dummy.refresh_from_db()
        self.assertEqual(dummy.language, 'fr_FR')

    def test_save_language_default(self):
        """
        Assume default language.
        """
        dummy = DummyPunchline.objects.create()
        dummy.refresh_from_db()
        self.assertEqual(dummy.language, 'en_US')
