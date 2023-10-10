from django.shortcuts import render
from django.apps import apps

from . import models


# Create your views here.
def homepage(request):
    movies = apps.get_model('content_creator', 'Movie').objects.all()
    series = apps.get_model('content_creator', 'Series').objects.all()

    context = {
        'movies': movies,
        'series': series,
    }

    return render(request, 'homepage.html', context)


def movies(request):
    content_movies = apps.get_model(app_label='content_creator', model_name='Movie').objects.all()
    continue_movies = apps.get_model(app_label='content_management', model_name='ContinueWatchingMoviePart').objects.all()
    recommended_movies = apps.get_model(app_label='content_management', model_name='FavouriteMovie').objects.all()
    trending_movies = apps.get_model(app_label='content_management', model_name='ShowCollectionMovie').objects.all()

    context = {
        'content_movies': content_movies,
        'continue_movies':continue_movies,
        'recommended_movies':recommended_movies,
        'trending_movies':trending_movies,
    }
    return render(request, 'subscriber/movies.html', context)


def movie_info(request,passed_id):
    content_movies = apps.get_model(app_label='content_creator', model_name='Movie').objects.get(id=passed_id)
    content_movies_part = apps.get_model(app_label='content_creator', model_name='MoviePart').objects.filter(movie_id=passed_id)
    movie_part_id = request.GET.get('movie-part') or content_movies_part.first().id
    content_movie_trailer = apps.get_model(app_label='content_creator', model_name='MovieTrailer').objects.filter(movie_part_id=movie_part_id)

    context = {
        'content_movies': content_movies,
        'content_movies_part': content_movies_part,
        'content_movie_trailer': content_movie_trailer,
    }
    return render(request, 'subscriber/movie_info.html', context)

def subscriber(request):
    return render(request, 'subscriber/subscriber.html')
def watchlist(request):
    mylist = apps.get_model('content_management', 'Watchlist').objects.all()

    return render(request, "mylist.html", {"mylist": mylist, })

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
