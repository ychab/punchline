from dal import autocomplete
from rest_framework.decorators import list_route
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from .models import Album, Artist, Punchline, Song
from .serializers import PunchlineSerializer


class PunchlineViewSet(ListModelMixin, GenericViewSet):
    """
    list:
    Returns a paginated list of punchlines.

    punch-it:
    Returns a random punchline.
    """
    model = Punchline
    queryset = Punchline.objects.order_by('-created')
    serializer_class = PunchlineSerializer
    permission_classes = (AllowAny,)
    filter_fields = ('artist',)
    search_fields = ('text',)

    @list_route(['get'])
    def punch_it(self, request, *args, **kwargs):
        # Random query could be dangerous for performance...?
        punchline = Punchline.objects.order_by('?')[:1].first()
        serializer = self.get_serializer(punchline)
        return Response(serializer.data)


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
