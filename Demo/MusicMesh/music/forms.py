from django import forms
from django.contrib.auth.models import User

from .models import Album, Song, Playlist


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        exclude = ['user']
        # fields = '__all__'

# class ContactForm(forms.Form):
#     contact_name = forms.CharField(required=True)
#     contact_email = forms.EmailField(required=True)
#     content = forms.CharField(
#         required=True,
#         widget=forms.Textarea
#     )
