from django.contrib import admin
from django.utils.encoding import force_text

from polymorphic.admin import PolymorphicParentModelAdmin

from punchline.apps.music.models import Artist, Song

from .models import Author, Punchline, Reference


@admin.register(Author)
class AuthorAdmin(PolymorphicParentModelAdmin):
    base_model = Author
    child_models = (Artist,)
    list_display = ('name',)
    # list_display_link = ('name',)

    def name(self, obj):
        import pdb; pdb.set_trace()
        return force_text(obj)


@admin.register(Reference)
class ReferenceAdmin(PolymorphicParentModelAdmin):
    base_model = Reference
    child_models = (Song,)


@admin.register(Punchline)
class PunchlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'modified', 'author', 'teaser')
    list_display_links = ('id',)
    list_select_related = ('author__artist', 'reference__song__album')
    search_fields = (
        'author__first_name',
        'author__last_name',
        'author__artist__nickname',
        'text',
    )
    date_hierarchy = 'created'
    ordering = ('-modified',)
    list_per_page = 50
