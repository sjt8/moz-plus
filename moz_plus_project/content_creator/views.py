from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import MoviePart, Series, Season, Episodes, Movie

from .forms import (
    AddMoviesForm,
    EditMovieForm,
    EditMoviePartForm,
    AddMoviePartForm,
    EditEpisodesForm,
    EditSeasonForm,
    EditSerieForm,
    MovieTrailerAddform,
)


from .forms import SeriesForm, SeasonForm, EpisodesForm
from crispy_bootstrap5.bootstrap5 import FloatingField
from django.contrib.auth.decorators import login_required


from . import models


@login_required
# Create your views here.
def content_creator(request):
    moz_user = models.ContentCreator.objects.get(user=request.user)
    return render(
        request, "content_creator/content_creator.html", {"moz_user": moz_user}
    )


@login_required
def series(request):
    moz_user = models.ContentCreator.objects.get(user=request.user)

    search = request.GET.get("search")

    if search:
        content_series = models.Series.objects.filter(creator=moz_user, title__icontains=search,)
    else:
        content_series = models.Series.objects.filter(creator=moz_user)

    context = {"content_series": content_series, "moz_user": moz_user}
    return render(request, "content_creator/series.html", context)


@login_required
def series_details(request, series_id=None, season_id=None):
    moz_user = models.ContentCreator.objects.get(user=request.user)

    content_series = models.Series.objects.get(id=series_id)
    content_seasons = models.Season.objects.filter(series_id=series_id)

    content_episodes = None
    content_season = None
    if season_id:
        content_season = models.Season.objects.get(id=season_id)
        content_episodes = models.Episodes.objects.filter(season_id=season_id)
    elif content_seasons:
        content_season = models.Season.objects.get(id=content_seasons.first().id)
        content_episodes = models.Episodes.objects.filter(
            season_id=content_seasons.first().id
        )

    search = request.GET.get("search")
    if search:
        content_episodes = content_episodes.filter(title__icontains=search)

    context = {
        "content_series": content_series,
        "content_seasons": content_seasons,
        "content_episodes": content_episodes,
        "content_season": content_season,
        "moz_user": moz_user,
    }
    return render(request, "content_creator/series_details.html", context)


@login_required
def add_season(request, series_id):
    if request.method == "POST":
        add_season_form = SeasonForm(request.POST, request.FILES)
        if add_season_form.is_valid():
            new_season = add_season_form.save(commit=False)
            new_season.post_author = request.user
            new_season.series_id = series_id
            new_season.save()

            return redirect(
                "content_creator:series_details", new_season.series.id, new_season.id
            )
    else:
        add_season_form = SeasonForm()
        return render(
            request,
            "content_creator/add_season.html",
            context={"add_season_form": add_season_form},
        )


@login_required
def add_episode(request, season_id):
    if request.method == "POST":
        add_episode_form = EpisodesForm(request.POST, request.FILES)
        if add_episode_form.is_valid():
            new_episode = add_episode_form.save(commit=False)
            new_episode.post_author = request.user
            new_episode.season_id = season_id
            new_episode.save()
            return redirect(
                "content_creator:series_details",
                new_episode.season.series.id,
                new_episode.season.id,
            )

    else:
        add_episode_form = EpisodesForm()

    return render(
        request,
        "content_creator/add_episode.html",
        context={"add_episode_form": add_episode_form},
    )


@login_required
def edit_season(request, series_id, passed_id):
    # get the get method var and passing  that along with the model
    season_details = get_object_or_404(Season, id=passed_id)
    edit_season_form = EditSeasonForm(
        request.POST or None, request.FILES or None, instance=season_details
    )
    if edit_season_form.is_valid():
        new_season = edit_season_form.save(commit=False)
        new_season.series_id = series_id
        new_season.save()
        return redirect(
            "content_creator:series_details", new_season.series.id, new_season.id
        )

    return render(
        request,
        "content_creator/edit_season.html",
        context={"edit_season_form": edit_season_form},
    )


@login_required
def edit_episode(request, season_id, passed_id):
    # get the get method var and passing  that along with the model
    episode_details = Episodes.objects.get(id=passed_id)
    edit_episode_form = EditEpisodesForm(
        request.POST or None, request.FILES or None, instance=episode_details
    )
    if edit_episode_form.is_valid():
        new_episode = edit_episode_form.save(commit=False)
        new_episode.season_id = season_id
        new_episode.save()
        return redirect(
            "content_creator:series_details",
            new_episode.season.series.id,
            new_episode.season.id,
        )

    return render(
        request,
        "content_creator/edit_episode.html",
        context={"edit_episode_form": edit_episode_form},
    )


@login_required
def delete_season(request, season_id):
    content_season = models.Season.objects.get(id=season_id)
    series_id = content_season.series.id
    content_season.delete()
    return redirect("content_creator:series_details", series_id)


# deleting the episode
@login_required
def delete_episode(request, episode_id):
    # get the get method var and passing  that along with the model
    content_episode = models.Episodes.objects.get(id=episode_id)
    season = content_episode.season
    content_episode.delete()
    return redirect("content_creator:series_details", season.series.id, season.id)


@login_required
def add_series(request):
    moz_user = models.ContentCreator.objects.get(user=request.user)

    if request.method == "POST":
        add_series_form = SeriesForm(request.POST, request.FILES)
        if add_series_form.is_valid():
            new_series = add_series_form.save(commit=False)
            new_series.creator = moz_user
            new_series.save()
            add_series_form.save_m2m()

            return redirect("content_creator:series")
    else:
        add_series_form = SeriesForm()

    return render(
        request, "content_creator/add_series.html", {"add_series_form": add_series_form}
    )


@login_required
def movies(request):
    moz_user = models.ContentCreator.objects.get(user=request.user)

    search = request.GET.get("search")
    if search:
        content_movies = models.Movie.objects.filter(creator=moz_user, title__icontains=search)
    else:
        content_movies = models.Movie.objects.filter(creator=moz_user)

    context = {"content_movies": content_movies, "moz_user": moz_user}
    return render(request, "content_creator/movies.html", context)


@login_required
def movie_details(request, movie_id):
    moz_user = models.ContentCreator.objects.get(user=request.user)

    content_movie = models.Movie.objects.get(id=movie_id)
    content_moviepart = models.MoviePart.objects.filter(movie_id=movie_id)

    search = request.GET.get("search")
    if search:
        content_moviepart = content_moviepart.filter(title__icontains=search)

    context = {
        "moz_user": moz_user,
        "content_movie": content_movie,
        "content_moviepart": content_moviepart,
    }
    return render(request, "content_creator/movie_details.html", context)


@login_required
def add_movies(request):
    moz_user = models.ContentCreator.objects.get(user=request.user)

    if request.method == "POST":
        add_movies_form = AddMoviesForm(request.POST, request.FILES)
        if add_movies_form.is_valid():
            new_movies = add_movies_form.save(commit=False)
            new_movies.creator = moz_user
            new_movies.save()
            add_movies_form.save_m2m()
            return redirect("content_creator:movies")
    else:
        add_movies_form = AddMoviesForm()

    return render(
        request, "content_creator/add_movies.html", {"add_movies_form": add_movies_form}
    )


@login_required
def add_moviespart(request, movie_id):
    if request.method == "POST":
        add_moviespart_form = AddMoviePartForm(request.POST, request.FILES)
        add_movietrailer_form = MovieTrailerAddform(request.POST)

        if add_moviespart_form.is_valid():
            new_moviepart = add_moviespart_form.save(commit=False)
            new_moviepart.movie_id = movie_id
            new_moviepart.save()
            new_movietrailer = add_movietrailer_form.save(commit=False)
            new_movietrailer.movie_part = new_moviepart
            new_movietrailer.save()
            return redirect("content_creator:movies_details", new_moviepart.movie.id)
    else:
        add_moviespart_form = AddMoviePartForm()
        add_movietrailer_form = MovieTrailerAddform()
    return render(
        request,
        "content_creator/add_moviepart.html",
        {
            "add_moviespart_form": add_moviespart_form,
            "add_movietrailer_form": add_movietrailer_form,
        },
    )


@login_required
def edit_movie(request, passed_id):
    # get the get method var and passing  that along with the model
    movie_details = get_object_or_404(Movie, id=passed_id)
    edit_movie_form = EditMovieForm(
        request.POST or None, request.FILES or None, instance=movie_details
    )
    if edit_movie_form.is_valid():
        new_movie = edit_movie_form.save(commit=False)
        new_movie.save()
        return redirect("content_creator:movies")

    return render(
        request,
        "content_creator/edit_movies.html",
        context={"edit_movie_form": edit_movie_form},
    )


@login_required
def edit_moviepart(request, passed_id):
    # get the get method var and passing  that along with the model
    moviepart_details = get_object_or_404(MoviePart, id=passed_id)
    edit_moviepart_form = EditMoviePartForm(
        request.POST or None, request.FILES or None, instance=moviepart_details
    )
    if edit_moviepart_form.is_valid():
        new_moviepart = edit_moviepart_form.save(commit=False)
        new_moviepart.save()
        return redirect("content_creator:movies_details", new_moviepart.movie.id)

    return render(
        request,
        "content_creator/edit_moviepart.html",
        context={"edit_moviepart_form": edit_moviepart_form},
    )


@login_required
def delete_moviepart(request, moviepart_id):
    content_moviepart = models.MoviePart.objects.get(id=moviepart_id)
    movie = content_moviepart.movie.id
    content_moviepart.delete()
    return redirect("content_creator:movies_details", movie)


@login_required
def delete_movie(request, movie_id):
    content_movie = models.Movie.objects.get(id=movie_id)
    content_movie.delete()
    return redirect("content_creator:movies")


@login_required
def edit_series(request, passed_id):
    # get the get method var and passing  that along with the model
    series_details = get_object_or_404(Series, id=passed_id)
    edit_series_form = EditSerieForm(
        request.POST or None, request.FILES or None, instance=series_details
    )
    if edit_series_form.is_valid():
        edit_series_form.save()
        return redirect("content_creator:series")

    return render(
        request,
        "content_creator/edit_series.html",
        context={"edit_series_form": edit_series_form},
    )


@login_required
def delete_series(request, series_id):
    content_series = models.Series.objects.get(id=series_id)
    content_series.delete()

    return redirect("content_creator:series")
