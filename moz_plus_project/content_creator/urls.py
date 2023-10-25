from django.urls import path


from . import views
from .views import (
    add_season,
    add_episode,
    edit_season,
    delete_season,
    delete_episode,
    add_series,
    edit_episode,
    add_movies,
    edit_moviepart,
    add_moviespart,
    edit_movie,
    delete_movie,
    delete_moviepart,
    edit_series,
    delete_series,
)

app_name = "content_creator"

urlpatterns = [
    path("content-creator/", views.content_creator, name="content_creator"),
    path("content-creator/series/", views.series, name="series"),
    path("content-creator/movies/", views.movies, name="movies"),
    path(
        "content-creator/series/<int:series_id>/",
        views.series_details,
        name="series_details",
    ),
    path(
        "content-creator/series/<int:series_id>/<int:season_id>/",
        views.series_details,
        name="series_details",
    ),
    path("content-creator/add-season/<int:series_id>/", add_season, name="add_season"),
    path("content-creator/add-episode/<int:season_id>/", add_episode, name="add_episode"),
    path(
        "content-creator/edit-season/<int:series_id>/<int:passed_id>/", edit_season, name="edit_season"
    ),
    path(
        "content-creator/delete_season/<int:season_id>/",
        delete_season,
        name="delete_season",
    ),
    path(
        "content-creator/delete_episode/<int:episode_id>/",
        delete_episode,
        name="delete_episode",
    ),
    path("content-creator/add-series/", add_series, name="add_series"),
    path(
        "content-creator/edit-episode/<int:season_id>/<int:passed_id>/",
        edit_episode,
        name="edit_episode",
    ),
    path(
        "content-creator/movie-details/<int:movie_id>/",
        views.movie_details,
        name="movies_details",
    ),
    path("content-creator/add-movies/", add_movies, name="add_movies"),
    path("content-creator/add-moviepart/<int:movie_id>/", add_moviespart, name="add_moviepart"),
    path("content-creator/edit-movie/<int:passed_id>/", edit_movie, name="edit_movie"),
    path(
        "content-creator/edit-moviepart/<int:passed_id>/",
        edit_moviepart,
        name="edit_moviepart",
    ),
    path(
        "content-creator/delete-movie/<int:movie_id>/",
        delete_movie,
        name="delete_movie",
    ),
    path(
        "content-creator/delete-moviepart/<int:moviepart_id>/",
        delete_moviepart,
        name="delete_moviepart",
    ),
    path(
        "content-creator/edit-series/<int:passed_id>/", edit_series, name="edit_series"
    ),
    path(
        "content-creator/delete-series/<int:series_id>/",
        delete_series,
        name="delete_series",
    ),
]
