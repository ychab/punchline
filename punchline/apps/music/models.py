from django.db import models
from django.utils.translation import ugettext_lazy as _

from punchline.apps.core.models import Author, Reference


class Artist(Author):
    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
        parent_link=True,
        related_name='artist',
    )
    nickname = models.CharField(max_length=1024)

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'artist'


class Album(models.Model):
    name = models.CharField(max_length=1024)
    date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'album'

    def __str__(self):
        return self.name


class Song(Reference):
    """
    A song could have further authors (including feat for example)
    """
    ref = models.OneToOneField(
        Reference,
        on_delete=models.CASCADE,
        parent_link=True,
        related_name='song',
    )

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

    class Meta:
        db_table = 'song'

    def __str__(self):
        return self.title

    def is_single(self):
        return not bool(self.album)
