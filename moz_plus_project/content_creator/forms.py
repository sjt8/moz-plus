from django import forms
from .models import (
    MoviePart,
    Series,
    Season,
    Episodes,
    Movie,
    MovieTrailer,
    SeasonTrailer,
)


class AddMoviesForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("title", "slug", "overview", "image")


class AddMoviePartForm(forms.ModelForm):

    class Meta:
        model = MoviePart
        fields = (
            "title",
            "slug",
            "part_no",
            "genre",
            "studio",
            "plot",
            "person",
            "release_date",
            "content_rating",
            "country",
            "language",
            "thumbnail",
            "video",
            "duration",
        )


class EditMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("title", "slug", "overview", "image")


class EditMoviePartForm(forms.ModelForm):
    class Meta:
        model = MoviePart
        fields = (
            "title",
            "slug",
            "part_no",
            "genre",
            "plot",
            "person",
            "release_date",
            "duration",
            "content_rating",
            "country",
            "language",
            "thumbnail",
            "video",
        )


# class for add form of series
class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ("title", "slug", "overview", "genre", "country", "image")


# class for add form of season
class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = (
            "season_no",
            "overview",
            "studio",
            "language",
            "release_date",
            "thumbnail",
        )


# class for add form of episode
class EpisodesForm(forms.ModelForm):
    class Meta:
        model = Episodes
        fields = (
            "title",
            "slug",
            "episode_no",
            "plot",
            "person",
            "release_date",
            "duration",
            "thumbnail",
            "video",
        )


# this the class for editing the series
class EditSerieForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ("title", "slug", "overview", "genre", "country", "image")


# this the class for editing the season
class EditSeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = (
            "season_no",
            "overview",
            "studio",
            "language",
            "release_date",
            "thumbnail",
        )


# this the class for editing the Episodes
class EditEpisodesForm(forms.ModelForm):
    class Meta:
        model = Episodes
        fields = (
            "title",
            "slug",
            "episode_no",
            "plot",
            "person",
            "release_date",
            "duration",
            "thumbnail",
            "video",
        )


class MovieTrailerAddform(forms.ModelForm):
    class Meta:
        model = MovieTrailer
        fields = ("url",)


class AddSeasonTrailerform(forms.ModelForm):
    class Meta:
        model = SeasonTrailer
        fields = ("url",)
