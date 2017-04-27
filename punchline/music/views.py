from dal import autocomplete

from .models import Album, Artist, Song

# punch it ! => returns a random punchline
# returns a punchliche with postgres seach text
# list all punchline, filtered by author


class ArtistAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Artist.objects.all()
        if self.q:
            qs = qs.filter(nickname__istartswith=self.q)
        qs = qs.order_by('nickname', '-pk')
        return qs


class AlbumAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Album.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        qs = qs.order_by('name', '-pk')
        return qs


class SongAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Song.objects.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)

        # Pre-filter song by artist of any.
        artist = self.forwarded.get('artist', None)
        if artist:
            qs = qs.filter(punchlines__artist=artist)
            qs = qs.distinct()

        qs = qs.order_by('title', '-pk')
        return qs
