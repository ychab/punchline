from django.db import models
from django.utils.translation import ugettext_lazy as _

from punchline.apps.core.models import Author


class Artist(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=1024)

    def __str__(self):
        return self.nickname


class Album(models.Model):
    name = models.CharField(max_length=1024)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    """
    A song could have further authors (including feat for example)
    """
    title = models.CharField(max_length=1024)
    album = models.ForeignKey(
        Album,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    date = models.DateField(
        null=True,
        blank=True,
        help_text=_('In cas this is a single (without album).'),
    )

    def is_single(self):
        return not bool(self.album)

    def __str__(self):
        return self.title
