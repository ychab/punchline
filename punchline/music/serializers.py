from rest_framework.serializers import ModelSerializer

from .models import Album, Artist, Punchline, Song


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(ModelSerializer):
    album = AlbumSerializer()

    class Meta:
        model = Song
        fields = '__all__'


class PunchlineSerializer(ModelSerializer):
    artist = ArtistSerializer()
    song = SongSerializer()

    class Meta:
        model = Punchline
        fields = '__all__'
