from django import forms

from .models import ShowRatingMoviePart, ShowRatingEpisodes


class ShowRatingMoviePartForm(forms.ModelForm):
    class Meta:
        model = ShowRatingMoviePart
        fields = ("rating",)


class ShowRatingEpisodesForm(forms.ModelForm):
    class Meta:
        model = ShowRatingEpisodes
        fields = ("rating",)