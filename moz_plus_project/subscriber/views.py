from django.shortcuts import render
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from . import models
from . import forms

from content_management.forms import ShowRatingMoviePartForm, ShowRatingEpisodesForm
from content_management.models import FavouriteMovie, FavouriteSeries


# Create your views here.
@login_required
def subscriber(request):
    moz_user = models.Subscriber.objects.get(user=request.user)

    movies = apps.get_model("content_creator", "Movie").objects.all()
    series = apps.get_model("content_creator", "Series").objects.all()

    context = {
        "movies": movies,
        "series": series,
        "moz_user": moz_user,
    }

    return render(request, "subscriber/subscriber.html", context)


@login_required
def movies(request):
    moz_user = models.Subscriber.objects.get(user=request.user)

    search = request.GET.get("search")

    if search:
        content_movies = apps.get_model(
            app_label="content_creator", model_name="Movie"
        ).objects.filter(title__icontains=search)
    else:
        content_movies = apps.get_model(
            app_label="content_creator", model_name="Movie"
        ).objects.all()

    context = {
        "content_movies": content_movies,
        "moz_user": moz_user,
    }
    return render(request, "subscriber/movies.html", context)


@login_required
def movie_info(request, passed_id):
    moz_user = models.Subscriber.objects.get(user=request.user)

    content_movies = apps.get_model(
        app_label="content_creator", model_name="Movie"
    ).objects.get(id=passed_id)

    content_movies_part = apps.get_model(
        app_label="content_creator", model_name="MoviePart"
    ).objects.filter(movie_id=passed_id)

    context = {
        "content_movies": content_movies,
        "content_movies_part": content_movies_part,
        "moz_user": moz_user,
    }
    return render(request, "subscriber/movie_info.html", context)


@login_required
def movie_part_details(request, movie_part_id):
    moz_user = models.Subscriber.objects.get(user=request.user)

    content_movies_part = apps.get_model(
        app_label="content_creator", model_name="MoviePart"
    ).objects.get(id=movie_part_id)

    content_movie_rating = (
        apps.get_model(app_label="content_management", model_name="ShowRatingMoviePart")
        .objects.filter(subscriber=moz_user, movie_part=content_movies_part)
        .first()
    )

    content_movie_trailer = apps.get_model(
        app_label="content_creator", model_name="MovieTrailer"
    ).objects.filter(movie_part_id=movie_part_id)

    favourite = FavouriteMovie.objects.filter(
        subscriber=moz_user, movie_part=content_movies_part
    ).first()

    if content_movie_rating:
        rating_form = ShowRatingMoviePartForm(instance=content_movie_rating)
    else:
        rating_form = ShowRatingMoviePartForm()

    if "rating" in request.POST:
        rating_form = ShowRatingMoviePartForm(
            request.POST, instance=content_movie_rating
        )

        if rating_form.is_valid():
            new_form = rating_form.save(commit=False)
            new_form.subscriber = moz_user
            new_form.movie_part = content_movies_part
            new_form.save()
    elif "favourite" in request.POST:
        if favourite:
            favourite.delete()
            favourite = None
        else:
            favourite = FavouriteMovie.objects.create(
                subscriber=moz_user, movie_part=content_movies_part
            )

    context = {
        "moz_user": moz_user,
        "content_movies_part": content_movies_part,
        "content_movie_rating": content_movie_rating,
        "content_movie_trailer": content_movie_trailer,
        "rating_form": rating_form,
        "favourite": favourite,
    }
    return render(request, "subscriber/moviepart_details.html", context)


@login_required
def series(request):
    moz_user = models.Subscriber.objects.get(user=request.user)

    search = request.GET.get("search")

    if search:
        content_series = apps.get_model(
            app_label="content_creator", model_name="Series"
        ).objects.filter(title__icontains=search)
    else:
        content_series = apps.get_model(
            app_label="content_creator", model_name="Series"
        ).objects.all()

    context = {
        "content_series": content_series,
        "moz_user": moz_user,
    }
    return render(request, "subscriber/series.html", context)


@login_required
def series_details(request, series_id, season_id=None):
    moz_user = models.Subscriber.objects.get(user=request.user)

    content_series = apps.get_model(
        app_label="content_creator", model_name="Series"
    ).objects.get(id=series_id)

    content_seasons = apps.get_model(
        app_label="content_creator", model_name="Season"
    ).objects.filter(series_id=series_id)

    content_season_id = season_id or content_seasons.first().id

    content_season = apps.get_model(
        app_label="content_creator", model_name="Season"
    ).objects.get(id=content_season_id)

    content_episodes = apps.get_model(
        app_label="content_creator", model_name="Episodes"
    ).objects.filter(season_id=content_season_id)

    content_season_trailer = apps.get_model(
        app_label="content_creator", model_name="SeasonTrailer"
    ).objects.filter(season_id=content_season_id)

    favourite = FavouriteSeries.objects.filter(
        subscriber=moz_user, series=content_series
    ).first()

    if "favourite" in request.POST:
        if favourite:
            favourite.delete()
            favourite = None
        else:
            favourite = FavouriteSeries.objects.create(
                subscriber=moz_user, series=content_series
            )

    context = {
        "content_series": content_series,
        "content_season": content_season,
        "content_seasons": content_seasons,
        "content_episodes": content_episodes,
        "content_season_trailer": content_season_trailer,
        "moz_user": moz_user,
        "favourite": favourite,
    }
    return render(request, "subscriber/series_details.html", context)


@login_required
def episode_details(request, series_id, season_id, episode_id):
    moz_user = models.Subscriber.objects.get(user=request.user)

    content_episode = apps.get_model(
        app_label="content_creator", model_name="Episodes"
    ).objects.get(id=episode_id)

    content_episode_rating = (
        apps.get_model(app_label="content_management", model_name="ShowRatingEpisodes")
        .objects.filter(subscriber=moz_user, episodes=content_episode)
        .first()
    )

    if content_episode_rating:
        rating_form = ShowRatingEpisodesForm(instance=content_episode_rating)
    else:
        rating_form = ShowRatingEpisodesForm()

    if "rating" in request.POST:
        rating_form = ShowRatingEpisodesForm(
            request.POST, instance=content_episode_rating
        )

        if rating_form.is_valid():
            new_form = rating_form.save(commit=False)
            new_form.subscriber = moz_user
            new_form.episodes = content_episode
            new_form.save()

    context = {
        "content_episode": content_episode,
        "moz_user": moz_user,
        "rating_form": rating_form,
    }
    return render(request, "subscriber/episode_details.html", context)


@login_required
def favourites(request):
    moz_user = models.Subscriber.objects.get(user=request.user)
    favourite_movie = FavouriteMovie.objects.filter(subscriber=moz_user)
    favourite_series = FavouriteSeries.objects.filter(subscriber=moz_user)

    context = {
        "moz_user": moz_user,
        "favourite_movie": favourite_movie,
        "favourite_series": favourite_series,
    }
    return render(request, "subscriber/favourites.html", context)
