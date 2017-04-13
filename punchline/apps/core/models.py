from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import truncatechars


class Author(models.Model):
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
        abstract = True

    def __str__(self):
        return self.fullname

    @property
    def fullname(self):
        return ' '.join([attr for attr in [self.first_name, self.last_name]])


class Reference(models.Model):
    class Meta:
        abstract = True


class Punchline(models.Model):
    # Unfortunetly, we cannot use Django Polymorphic due to abstract model...
    author_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    author_id = models.PositiveIntegerField()
    author_object = GenericForeignKey('author_type', 'author_id')

    ref_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name='punchlines')
    ref_id = models.PositiveIntegerField()
    ref_object = GenericForeignKey('ref_type', 'ref_id')

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'punchline'

    def __str__(self):
        return self.teaser

    @property
    def teaser(self):
        return truncatechars(self.text, 30)
