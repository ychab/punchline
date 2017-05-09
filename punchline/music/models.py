from django.db import models
from django.utils.translation import ugettext_lazy as _

from punchline.core.models import Author, Punchline as BasePunchline


class Artist(Author):
    nickname = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname


class Album(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='albums', null=True, blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=1024)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    album = models.ForeignKey(
        Album,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    date = models.DateField(
        null=True,
        blank=True,
        help_text=_('In case this is a single (without album).'),
    )

    def __str__(self):
        return self.title


class Punchline(BasePunchline):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(
        Song,
        on_delete=models.SET_NULL,
        related_name='punchlines',
        null=True,
        blank=True,
    )
