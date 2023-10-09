from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import MoviePart, Series, Season, Episodes, Movie
from .forms import AddMoviesForm, AddMoviePartForm, EditMovieForm, EditEpisodesForm, EditSeasonForm, EditSeiresForm
from .forms import SeriesForm, SeasonForm, EpisodesForm
from crispy_bootstrap5.bootstrap5 import FloatingField


# Create your views here.


def add_movie(request):
    if request.method == 'POST':
        movie_form = AddMoviesForm(request.POST, request.FILES)
        moviepart_form = AddMoviePartForm(request.POST)

        if movie_form.is_valid() and moviepart_form.is_valid():
            movie = movie_form.save()
            movie_part = moviepart_form.save(commit=False)
            movie_part.movie = movie

            moviepart_form.instance.movie = movie
            moviepart_form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        movie_form = AddMoviesForm()
        moviepart_form = AddMoviePartForm()

    return render(request, 'add_movie.html', {
        'movie_form': movie_form,
        'moviepart_form': moviepart_form,

    })


"""def add_movie(request):
    if request.method == 'POST':
        add_movie_form = AddMovieForm(request.POST, request.FILES)
        if add_movie_form.is_valid():
            new_movie = add_movie_form.save(commit=False)
            new_movie.post_author = request.user
            new_movie.save()
            return redirect('home_path')

    else:
        add_movie_form = AddMovieForm()

    return render(request, 'add_movie.html', {'add_movie_form':add_movie_form})"""


def edit_movie(request, passed_id):
    # get the get method var and passing  that along with the model
    movie_details = get_object_or_404(MoviePart, id=passed_id)
    edit_movie_form = EditMovieForm(request.POST or None, request.FILES or None, instance=movie_details)
    if edit_movie_form.is_valid():
        edit_movie_form.save()
        return redirect('home_path')
    return render(request, 'edit_movie.html', context={'edit_movie_form': edit_movie_form})


def add_series(request):
    if request.method == 'POST':
        series_form = SeriesForm(request.POST, request.FILES)
        season_form = SeasonForm(request.POST)
        episodes_form = EpisodesForm(request.POST)

        if series_form.is_valid() and season_form.is_valid() and episodes_form.is_valid():
            series = series_form.save()
            season = season_form.save(commit=False)
            season.series = series
            season.save()
            episodes_form.instance.season = season
            episodes_form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        series_form = SeriesForm()
        season_form = SeasonForm()
        episodes_form = EpisodesForm()

    return render(request, 'add_series.html', {
        'series_form': series_form,
        'season_form': season_form,
        'episodes_form': episodes_form,
    })


def edit_series(request, passed_id):
    # get the get method var and passing  that along with the model
    episode = Episodes.objects.filter(id=passed_id).first()
    season = Season.objects.filter(id=episode.season.id).first()
    series = Series.objects.filter(id=season.series.id).first()

    edit_series_form = EditSeiresForm(request.POST or None, instance=series or None)
    edit_season_form = EditSeasonForm(request.POST or None, instance=season or None)
    edit_episode_form = EditEpisodesForm(request.POST or None, request.FILES or None, instance=episode or None)
    if edit_episode_form.is_valid():
        edit_episode_form.save()

    # get the season id by filter
    if edit_season_form.is_valid():
        edit_season_form.save()

    # get the series id by filter from model series
    if edit_series_form.is_valid():
        edit_series_form.save()

    return render(request, 'edit_series.html', context={
        'edit_series_form': edit_series_form,
        'edit_episode_form': edit_episode_form,
        'edit_season_form': edit_season_form})


#  deleting the movie
def delete_movie(request, passed_id):
    # get the get method var and passing  that along with the model
    movie_details = get_object_or_404(Movie, id=passed_id)
    movie_details.delete()
    return redirect('home_path')


# deleting the series
def delete_series(request, passed_id):
    # get the get method var and passing  that along with the model
    series_details = get_object_or_404(Series, id=passed_id)
    series_details.delete()
    return redirect('home_path')


# delete the season

def delete_Season(request, passed_id):
    # get the get method var and passing  that along with the model
    Season_details = get_object_or_404(Season, id=passed_id)
    Season_details.delete()
    return redirect('home_path')


# deleting the episode

def delete_episode(request, passed_id):
    # get the get method var and passing  that along with the model
    episode_details = get_object_or_404(Episodes, id=passed_id)
    episode_details.delete()
    return redirect('home_path')


# searching the movie
def search_movie(request):
    # get the search term posted from the form with name 'searchpost'
    search_term = request.GET.get('searchmovie')
    if search_term:
        # if there is a vaild search term ,filter the list of objects with it
        movie_list = Movie.objects.filter(title__icontains=search_term)
    else:
        movie_list = Movie.objects.all()


# searching the series
def search_series(request):
    # get the search term posted from the form with name 'searchpost'
    search_term = request.GET.get('searchseries')
    if search_term:
        # if there is a vaild search term ,filter the list of objects with it
        Series_list = Series.objects.filter(title__icontains=search_term)
    else:
        series_list = Series.objects.all()

# listing the series in series


def series_list(request, passed_id):
    series_list = Series.objects.all()
    context = {'series_list': series_list}
    return render(request, 'series_page.html', context)