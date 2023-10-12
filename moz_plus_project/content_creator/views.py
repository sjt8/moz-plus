from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import MoviePart, Series, Season, Episodes, Movie
from .forms import AddMoviesForm,EditMovieForm,EditMoviePartForm,AddMoviePartForm,EditEpisodesForm,EditSeasonForm,EditSerieForm
from .forms import SeriesForm, SeasonForm, EpisodesForm
from crispy_bootstrap5.bootstrap5 import FloatingField
from django.contrib.auth.decorators import login_required


from . import models

@login_required
# Create your views here.
def content_creator(request):
    moz_user = models.ContentCreator.objects.get(user=request.user)
    return render(request, 'content_creator/content_creator.html', {'moz_user': moz_user})

@login_required
def series(request):
    moz_user = models.ContentCreator.objects.get(user=request.user)

    content_series = models.Series.objects.all()

    context = {
        'content_series': content_series,
        'moz_user': moz_user
    }
    return render(request, 'content_creator/series.html', context)

@login_required
def series_details(request, series_id):
    moz_user = models.ContentCreator.objects.get(user=request.user)

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
        'moz_user': moz_user,
    }
    return render(request, 'content_creator/series_details.html', context)



@login_required
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

@login_required
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



@login_required
def edit_season(request, passed_id):
    # get the get method var and passing  that along with the model
    season_details = get_object_or_404(Season,id=passed_id)
    edit_season_form =EditSeasonForm (request.POST or None, request.FILES or None,instance=season_details)
    if edit_season_form.is_valid():
        new_season = edit_season_form.save(commit=False)
        new_season.save()
        return redirect('content_creator:series_details', new_season.series.id)

    return render(request, 'content_creator/edit_season.html', context={'edit_season_form': edit_season_form})

@login_required
def edit_episode(request, passed_id):
    # get the get method var and passing  that along with the model
    episode_details = Episodes.objects.get(id=passed_id)
    edit_episode_form =EditEpisodesForm (request.POST or None, request.FILES or None,instance=episode_details)
    if edit_episode_form.is_valid():
        new_episode=edit_episode_form.save(commit=False)
        new_episode.save()
        return redirect('content_creator:series_details', new_episode.season.series.id)

    return render(request, 'content_creator/edit_episode.html', context={'edit_episode_form': edit_episode_form})

@login_required
def delete_Season(request, season_id):
    content_season = models.Season.objects.get(id=season_id)
    series_id = content_season.series.id
    content_season.delete()
    return redirect('content_creator:series_details', series_id)


# deleting the episode
@login_required
def delete_episode(request, episode_id):
    # get the get method var and passing  that along with the model
    content_episode = models.Episodes.objects.get(id=episode_id)
    series_id = content_episode.season.series.id
    content_episode.delete()
    return redirect('content_creator:series_details',series_id)





@login_required
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

@login_required
def movies(request):
    moz_user = models.ContentCreator.objects.get(user=request.user)

    content_movies = models.Movie.objects.all()

    context = {
        'content_movies': content_movies,
        'moz_user': moz_user
    }
    return render(request, 'content_creator/movies.html', context)
@login_required
def movie_details(request,movie_id):
    content_movie = models.Movie.objects.get(id=movie_id)
    content_moviepart = models.MoviePart.objects.filter(movie_id=movie_id)

    if request.GET.get('moviepart'):
        moviepart_id = request.GET.get('moviepart')
    elif content_moviepart.first():
        moviepart_id = content_moviepart.first().id
    else:
        moviepart_id = 0


    context = {
        'content_movie': content_movie,
        'content_moviepart': content_moviepart,

        'moviepart_id': moviepart_id,
    }
    return render(request, 'content_creator/movie_details.html', context)

@login_required
def add_movies(request):
    if request.method == 'POST':
        add_movies_form =AddMoviesForm(request.POST, request.FILES)
        if add_movies_form.is_valid():
            new_movies = add_movies_form.save(commit=False)
            new_movies.post_author = request.user
            new_movies.save()
            return redirect('content_creator:movies')
    else:
        add_movies_form = AddMoviesForm()

    return render(request, 'content_creator/add_movies.html', {'add_movies_form': add_movies_form})

@login_required
def add_moviespart(request):
    if request.method == 'POST':
        add_moviespart_form =AddMoviePartForm(request.POST, request.FILES)
        if add_moviespart_form.is_valid():
            new_moviepart= add_moviespart_form.save(commit=False)
            new_moviepart.post_author = request.user
            new_moviepart.save()
            return redirect('content_creator:movies_details', new_moviepart.movie.id)
    else:
        add_moviespart_form = AddMoviePartForm()

    return render(request, 'content_creator/add_moviepart.html', {'add_moviespart_form': add_moviespart_form})


@login_required
def edit_movie(request, passed_id):
    # get the get method var and passing  that along with the model
    movie_details = get_object_or_404(Movie,id=passed_id)
    edit_movie_form =EditMovieForm (request.POST or None, request.FILES or None,instance=movie_details)
    if edit_movie_form.is_valid():
        new_movie = edit_movie_form.save(commit=False)
        new_movie.save()
        return redirect('content_creator:movies')

    return render(request, 'content_creator/edit_movies.html', context={'edit_movie_form':edit_movie_form})


@login_required
def edit_moviepart(request, passed_id):
    # get the get method var and passing  that along with the model
    moviepart_details = get_object_or_404(MoviePart,id=passed_id)
    edit_moviepart_form =EditMoviePartForm(request.POST or None, request.FILES or None,instance=moviepart_details)
    if edit_moviepart_form.is_valid():
        new_moviepart = edit_moviepart_form.save(commit=False)
        new_moviepart.save()
        return redirect('content_creator:movies_details', new_moviepart.movie.id)

    return render(request, 'content_creator/edit_moviepart.html', context={'edit_moviepart_form': edit_moviepart_form})


@login_required
def delete_moviepart(request,moviepart_id):
    content_moviepart = models.MoviePart.objects.get(id=moviepart_id)
    movie = content_moviepart.movie.id
    content_moviepart.delete()
    return redirect('content_creator:movies_details', movie)


@login_required
def delete_movie(request,movie_id):
    content_movie = models.Movie.objects.get(id=movie_id)
    content_movie.delete()
    return redirect('content_creator:movies')


@login_required
def edit_series(request, passed_id):
    # get the get method var and passing  that along with the model
    series_details = get_object_or_404(Series,id=passed_id)
    edit_series_form =EditSerieForm (request.POST or None, request.FILES or None,instance=series_details )
    if edit_series_form.is_valid():
        new_series = edit_series_form.save(commit=False)
        new_series.save()
        return redirect('content_creator:series')

    return render(request, 'content_creator/edit_series.html', context={'edit_series_form':edit_series_form})


@login_required
def delete_series(request,series_id):
    content_series = models. Series.objects.get(id=series_id)
    content_series.delete()
    return redirect('content_creator:series')


