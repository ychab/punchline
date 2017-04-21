from django.db import models
from django.template.defaultfilters import truncatechars

from polymorphic.models import PolymorphicModel


class Author(PolymorphicModel):
    """
    An author of a punchline is not necessary an artist.
    It could be a politician, celebrity, and so on.
    """
    first_name = models.CharField(max_length=512, null=True, blank=True)
    last_name = models.CharField(max_length=512, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='authors', null=True, blank=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.fullname

    @property
    def fullname(self):
        return ' '.join([attr for attr in [self.first_name, self.last_name] if attr])


class Reference(PolymorphicModel):
    class Meta:
        db_table = 'reference'


class Punchline(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='punchlines',
    )
    reference = models.ForeignKey(
        Reference,
        on_delete=models.CASCADE,
        related_name='punchlines',
    )

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'punchline'

    def __str__(self):
        return self.teaser

    @property
    def teaser(self):
        return truncatechars(self.text, 30)
