from django.contrib import admin

from .models import Author, Punchline


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname',)
    list_select_related = ('artist',)


@admin.register(Punchline)
class PunchlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'modified', 'author', 'teaser')
    list_display_links = ('id',)
    list_select_related = ('author__artist', 'song__album')
    search_fields = (
        'author__first_name',
        'author__last_name',
        'author__artist__nickname',
        'text',
    )
    date_hierarchy = 'created'
    ordering = ('-modified',)
    list_per_page = 50
