from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)

from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/login/", views.user_login, name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path(
        "accounts/password-change/",
        PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "accounts/password-change-done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("register/", views.subscriber_registration, name="register"),
    path(
        "content-creator/register/", views.creator_registration, name="register_creator"
    ),
    path("home/series/", views.series, name="series"),
    path(
        "home/series/<int:series_id>/",
        views.series_details,
        name="series_details",
    ),
    path(
        "home/series/<int:series_id>/<int:season_id>/",
        views.series_details,
        name="series_details",
    ),
    path(
        "home/series/<int:series_id>/<int:season_id>/<int:episode_id>/",
        views.episode_details,
        name="episode_details",
    ),
    path("home/movies/", views.movies, name="movies"),
    path("home/movie-info/<int:passed_id>/", views.movie_info, name="movie_info"),
    path(
        "home/movie-part/<int:movie_part_id>/",
        views.movie_part_details,
        name="movie_part_details",
    ),
]
