from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import MoviePart, Series, Season, Episodes, Movie
from .forms import AddMoviesForm, AddMoviePartForm, EditMovieForm, EditEpisodesForm, EditSeasonForm, EditSeiresForm
from .forms import SeriesForm, SeasonForm, EpisodesForm
from crispy_bootstrap5.bootstrap5 import FloatingField


from . import models


# Create your views here.
def content_creator(request):
    return render(request, 'content_creator/content_creator.html')


def series(request):
    content_series = models.Series.objects.all()

    context = {
        'content_series': content_series
    }
    return render(request, 'content_creator/series.html', context)


def series_details(request, series_id):
    content_series = models.Series.objects.get(id=series_id)
    content_season = models.Season.objects.filter(series_id=series_id)
    season_id = request.GET.get('season') or content_season.first().id
    content_episodes = models.Episodes.objects.filter(season_id=season_id)

    context = {
        'content_series': content_series,
        'content_season': content_season,
        'content_episodes': content_episodes,
    }
    return render(request, 'content_creator/series_details.html', context)