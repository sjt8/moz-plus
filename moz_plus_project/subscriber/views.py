from django.shortcuts import render
from django.apps import apps
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.shortcuts import redirect
from . import models


# Create your views here.


@login_required
def subscriber(request):

    moz_user = models.Subscriber.objects.get(user=request.user)

    movies = apps.get_model('content_creator', 'Movie').objects.all()
    series = apps.get_model('content_creator', 'Series').objects.all()

    context = {
        'movies': movies,
        'series': series,
        'moz_user': moz_user,
    }

    return render(request, 'subscriber/subscriber.html', context)

@login_required
def movies(request):
    moz_user = models.Subscriber.objects.get(user=request.user)

    content_movies = apps.get_model(app_label='content_creator', model_name='Movie').objects.all()
    recommended_movies = apps.get_model(app_label='content_management', model_name='FavouriteMovie').objects.all()
    trending_movies = apps.get_model(app_label='content_management', model_name='ShowCollectionMovie').objects.all()
    if apps.get_model(app_label='content_management', model_name='ContinueWatchingMoviePart').objects.filter(subscriber_id= request.user.id).exists():
        continue_movies = apps.get_model(app_label='content_management',
                                         model_name='ContinueWatchingMoviePart').objects.filter(subscriber_id=request.user.id)
    else:
        continue_movies = None

    context = {
        'content_movies': content_movies,
        'continue_movies':continue_movies,
        'recommended_movies':recommended_movies,
        'trending_movies':trending_movies,
        'moz_user': moz_user,
    }
    return render(request, 'subscriber/movies.html', context)


@login_required
def movie_info(request,passed_id):
    moz_user = models.Subscriber.objects.get(user=request.user)

    content_movies = apps.get_model(app_label='content_creator', model_name='Movie').objects.get(id=passed_id)
    content_movies_part = apps.get_model(app_label='content_creator', model_name='MoviePart').objects.filter(movie_id=passed_id)
    movie_part_id = request.GET.get('movie-part') or content_movies_part.first().id
    content_movie_trailer = apps.get_model(app_label='content_creator', model_name='MovieTrailer').objects.filter(movie_part_id=movie_part_id)
    rating = apps.get_model(app_label='content_management', model_name='ShowRatingMoviePart').objects.filter(subscriber_id= request.user.id,movie_part_id=passed_id).values
    context = {
        'content_movies': content_movies,
        'content_movies_part': content_movies_part,
        'content_movie_trailer': content_movie_trailer,
        'moz_user': moz_user,
        'rating':rating,
    }
    return render(request, 'subscriber/movie_info.html', context)


@login_required
def watchlist(request,user_id):
    moz_user = models.Subscriber.objects.get(user=request.user)

    mylist = apps.get_model('content_management', 'WatchlistMoviesPart').objects.filter(subscriber_id= user_id)
    context = {"mylist": mylist,'moz_user': moz_user,}

    return render(request, "subscriber/mylist.html",context )

@login_required
def series(request):
    moz_user = models.Subscriber.objects.get(user=request.user)

    content_series = apps.get_model(app_label='content_creator', model_name='Series').objects.all()
    trending_series = apps.get_model(app_label='content_management', model_name='ShowCollectionSeries').objects.all()
    context = {
        'content_series': content_series,
        'trending_series':trending_series,
        'moz_user': moz_user,
    }
    return render(request, 'subscriber/series.html', context)


@login_required
def series_details(request, series_id):
    moz_user = models.Subscriber.objects.get(user=request.user)

    content_series = apps.get_model(app_label='content_creator', model_name='Series').objects.get(id=series_id)
    content_season = apps.get_model(app_label='content_creator', model_name='Season').objects.filter(series_id=series_id)
    season_id = request.GET.get('season') or content_season.first().id
    content_episodes = apps.get_model(app_label='content_creator', model_name='Episodes').objects.filter(season_id=season_id)
    content_season_trailer = apps.get_model(app_label='content_creator', model_name='SeasonTrailer').objects.filter(season_id=season_id)

    context = {
        'content_series': content_series,
        'content_season': content_season,
        'content_episodes': content_episodes,
        'content_season_trailer': content_season_trailer,
        'moz_user': moz_user,
    }
    return render(request, 'subscriber/series_details.html', context)

@login_required
def add_to_watchlist(request, passed_id):
    # Get the logged-in user
    user = models.Subscriber.objects.get(user=request.user)

    # Check if the user is logged in
    if user.is_authenticated:
        # Get the movie based on the movie_id
        movie = apps.get_model(app_label='content_creator', model_name='MoviePart').objects.filter(movie_id=passed_id)

        # Create or get the WatchlistMoviesPart object for the user
        watchlist, created = apps.get_model('content_management', 'WatchlistMoviesPart').objects.get_or_create(subscriber=user.subscriber)

        # Add the movie to the watchlist
        watchlist.movies.add(movie)

        # Optionally, you can add a message to indicate success
        messages.success(request, f'{movie.title} has been added to your watchlist.')

    # Redirect the user back to the movie detail page or any other appropriate page
    return redirect('subscriber:movie_info', movie_id=passed_id)
