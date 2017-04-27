from django import forms

from dal import autocomplete

from .models import Punchline, Song


class SongAdminForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = '__all__'
        widgets = {
            'album': autocomplete.ModelSelect2(url='admin:album-autocomplete'),
        }


class PunchlineAdminForm(forms.ModelForm):

    class Meta:
        model = Punchline
        fields = '__all__'
        widgets = {
            'artist': autocomplete.ModelSelect2(url='admin:artist-autocomplete'),
            'song': autocomplete.ModelSelect2(
                url='admin:song-autocomplete',
                forward=['artist'],
            ),
        }
