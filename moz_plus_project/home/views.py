from django.apps import apps
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from . import forms


# Create your views here.
def home(request):
    return render(request, "home/home.html")


def user_login(request):
    if request.method != "POST":
        form = forms.LoginForm()
    else:
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            auth = authenticate(
                request,
                username=data["username"],
                password=data["password"],
            )

            if auth is not None:
                login(request, auth)
                if request.user.is_superuser:
                    return redirect("super_admin:super_admin")
                elif request.user.groups.all().first().name == "content_creator":
                    return redirect("content_creator:content_creator")
                elif request.user.groups.all().first().name == "subscriber":
                    return redirect("subscriber:subscriber")

    context = {"form": form}
    return render(request, "registration/login.html", context)


def subscriber_registration(request):
    if request.method != "POST":
        form = forms.UserRegistrationForm()
    else:
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            group_reviewer = Group.objects.get(name="subscriber")
            new_user.groups.add(group_reviewer)

            return redirect("subscriber:subscriber")

    context = {"form": form}
    return render(request, "accounts/user_registration.html", context)


def creator_registration(request):
    if request.method != "POST":
        form = forms.CreatorRegistrationForm()
    else:
        form = forms.CreatorRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            group_reviewer = Group.objects.get(name="content_creator")
            new_user.groups.add(group_reviewer)

            return redirect("content_creator:content_creator")

    context = {"form": form}
    return render(request, "accounts/creator_registration.html", context)


def movies(request):
    search = request.GET.get("search")

    if search:
        content_movies = apps.get_model(
            app_label="content_creator", model_name="Movie"
        ).objects.filter(title__icontains=search)
    else:
        content_movies = apps.get_model(
            app_label="content_creator", model_name="Movie"
        ).objects.all()

    context = {"content_movies": content_movies}
    return render(request, "home/movie/movies.html", context)


def movie_info(request, passed_id):
    content_movies = apps.get_model(
        app_label="content_creator", model_name="Movie"
    ).objects.get(id=passed_id)

    content_movies_part = apps.get_model(
        app_label="content_creator", model_name="MoviePart"
    ).objects.filter(movie_id=passed_id)

    context = {
        "content_movies": content_movies,
        "content_movies_part": content_movies_part,
    }

    return render(request, "home/movie/movie_info.html", context)


def movie_part_details(request, movie_part_id):
    content_movies_part = apps.get_model(
        app_label="content_creator", model_name="MoviePart"
    ).objects.get(id=movie_part_id)

    content_movie_rating = (
        apps.get_model(app_label="content_management", model_name="ShowRatingMoviePart")
        .objects.filter(movie_part=content_movies_part)
        .first()
    )

    content_movie_trailer = apps.get_model(
        app_label="content_creator", model_name="MovieTrailer"
    ).objects.filter(movie_part_id=movie_part_id)

    context = {
        "content_movies_part": content_movies_part,
        "content_movie_rating": content_movie_rating,
        "content_movie_trailer": content_movie_trailer,
    }
    return render(request, "home/movie/moviepart_details.html", context)


def series(request):
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
    }
    return render(request, "home/series/series.html", context)


def series_details(request, series_id, season_id=None):
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

    context = {
        "content_series": content_series,
        "content_season": content_season,
        "content_seasons": content_seasons,
        "content_episodes": content_episodes,
        "content_season_trailer": content_season_trailer,
    }
    return render(request, "home/series/series_details.html", context)


def episode_details(request, series_id, season_id, episode_id):
    content_episode = apps.get_model(
        app_label="content_creator", model_name="Episodes"
    ).objects.get(id=episode_id)

    context = {
        "content_episode": content_episode,
    }
    return render(request, "home/series/episode_details.html", context)
