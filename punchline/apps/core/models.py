from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.encoding import force_text


class Author(models.Model):
    """
    An author of a punchline is not be necessary an artist!
    It could be a politician, celebrity, and so on.
    """
    first_name = models.CharField(max_length=512, null=True, blank=True)
    last_name = models.CharField(max_length=512, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='authors', null=True, blank=True)

    def __str__(self):
        return self.fullname

    @property
    def fullname(self):

        return ' '.join([self.first_name, self.last_name])


class Punchline(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    song = models.ForeignKey(
        'music.Song',
        on_delete=models.SET_NULL,  # Could be used by another punchline
        related_name='punchlines',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.teaser

    @property
    def author_repr(self):
        if self.author.artist:
            return force_text(self.author.artist)
        return self.author

    @property
    def teaser(self):
        return truncatechars(self.text, 30)
