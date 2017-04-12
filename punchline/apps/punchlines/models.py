from django.db import models


class Author(models.Model):
    """
    An author of a punchline is not be necessary an artist!
    It could be a politician, celebrity, and so on.
    """
    first_name = models.CharField(max_length=512, null=True, blank=True)
    last_name = models.CharField(max_length=512, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Artist(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)


class Album(models.Model):
    name = models.CharField(max_length=1024)
    release_date = models.DateField(null=True, blank=True)


class Song(models.Model):
    title = models.CharField(max_length=1024)
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def is_single(self):
        return not bool(self.album)


class Punchline(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()

    song = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    # album = models.ForeignKey(
    #     Album,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    # )
