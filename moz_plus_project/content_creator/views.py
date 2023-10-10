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

    if request.GET.get('season'):
        season_id = request.GET.get('season')
    elif content_season.first():
        season_id = content_season.first().id
    else:
        season_id = 0

    content_episodes = models.Episodes.objects.filter(season_id=season_id)

    context = {
        'content_series': content_series,
        'content_season': content_season,
        'content_episodes': content_episodes,
        'season_id': season_id,
    }
    return render(request, 'content_creator/series_details.html', context)




def add_season(request):
    if request.method == 'POST':
        add_season_form = SeasonForm(request.POST, request.FILES)
        if add_season_form.is_valid():
            new_season = add_season_form.save(commit=False)
            new_season.post_author = request.user
            new_season.save()
            return redirect('content_creator:series_details',new_season.series.id)

    else:
        add_season_form = SeasonForm()

    return render(request, 'content_creator/add_season.html', context={'add_season_form': add_season_form})

def add_episode(request):
    if request.method == 'POST':
        add_episode_form = EpisodesForm(request.POST, request.FILES)
        if add_episode_form.is_valid():
            new_episode = add_episode_form.save(commit=False)
            new_episode.post_author = request.user
            new_episode.save()
            return redirect('content_creator:series_details',new_episode.season.series.id)

    else:
        add_episode_form = EpisodesForm()

    return render(request, 'content_creator/add_episode.html', context={'add_episode_form': add_episode_form})


def edit_season(request, passed_id):
    # get the get method var and passing  that along with the model
    season_details = get_object_or_404(Season,id=passed_id)
    edit_season_form =EditSeasonForm (request.POST or None, request.FILES or None,instance=season_details)
    if edit_season_form.is_valid():
        new_season = edit_season_form.save(commit=False)
        new_season.save()
        return redirect('content_creator:series_details', new_season.series.id)

    return render(request, 'content_creator/edit_season.html', context={'edit_season_form': edit_season_form})

def edit_episode(request, passed_id):
    # get the get method var and passing  that along with the model
    episode_details = Episodes.objects.get(id=passed_id)
    edit_episode_form =EditEpisodesForm (request.POST or None, request.FILES or None,instance=episode_details)
    if edit_episode_form.is_valid():
        new_episode=edit_episode_form.save(commit=False)
        new_episode.save()
        return redirect('content_creator:series_details', new_episode.season.series.id)

    return render(request, 'content_creator/edit_episode.html', context={'edit_episode_form': edit_episode_form})


def delete_Season(request, season_id):
    content_season = models.Season.objects.get(id=season_id)
    series_id = content_season.series.id
    content_season.delete()
    return redirect('content_creator:series_details', series_id)


# deleting the episode

def delete_episode(request, episode_id):
    # get the get method var and passing  that along with the model
    content_episode = models.Episodes.objects.get(id=episode_id)
    series_id = content_episode.season.series.id
    content_episode.delete()
    return redirect('content_creator:series_details',series_id)






def add_series(request):
    if request.method == 'POST':
        add_series_form =SeriesForm(request.POST, request.FILES)
        if add_series_form.is_valid():
            new_series = add_series_form.save(commit=False)
            new_series.post_author = request.user
            new_series.save()
            return redirect('content_creator:series')
    else:
        add_series_form = SeriesForm()

    return render(request, 'content_creator/add_series.html', {'add_series_form': add_series_form })
