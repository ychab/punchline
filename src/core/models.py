from django.conf import settings
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import get_language, to_locale


class Author(models.Model):
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
        return ' '.join([self.first_name, self.last_name])


class Punchline(models.Model):
    text = models.TextField()
    language = models.CharField(max_length=6, default='', editable=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.teaser

    def save(self, *args, **kwargs):
        if self.pk is None and not self.language:
            language_code = get_language() or settings.LANGUAGE_CODE
            self.language = to_locale(language_code)
        super().save(*args, **kwargs)

    @property
    def teaser(self):
        return truncatechars(self.text, 50)
