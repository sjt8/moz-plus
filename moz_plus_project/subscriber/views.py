from django.shortcuts import render
from django.apps import apps

from . import models


# Create your views here.
def subscriber(request):
    return render(request, 'subscriber/subscriber.html')


def series(request):

    content_series = apps.get_model(app_label='content_creator', model_name='Series').objects.all()

    context = {
        'content_series': content_series
    }
    return render(request, 'subscriber/series.html', context)


def series_details(request, series_id):

    content_series = apps.get_model(app_label='content_creator', model_name='Series').objects.get(id=series_id)
    content_season = apps.get_model(app_label='content_creator', model_name='Season').objects.filter(series_id=series_id)
    season_id = request.GET.get('season') or content_season.first().id
    content_episodes = apps.get_model(app_label='content_creator', model_name='Episodes').objects.filter(season_id=season_id)
    content_season_trailer = apps.get_model(app_label='content_creator', model_name='SeasonTrailer').objects.filter(season_id=season_id)

    context = {
        'content_series': content_series,
        'content_season': content_season,
        'content_episodes': content_episodes,
        'content_season_trailer':content_season_trailer,
    }
    return render(request, 'subscriber/series_details.html', context)
