from django.urls import path

from . import views

app_name = 'subscriber'

urlpatterns = [
    path('subscriber/', views.subscriber, name='subscriber'),
    path('subscriber/series/', views.series, name='series'),
    path(
        "subscriber/series/<int:series_id>/",
        views.series_details,
        name="series_details",
    ),
    path(
        "subscriber/series/<int:series_id>/<int:season_id>/",
        views.series_details,
        name="series_details",
    ),
    path(
        "subscriber/series/<int:series_id>/<int:season_id>/<int:episode_id>/",
        views.episode_details,
        name="episode_details",
    ),
    path('subscriber/movies/', views.movies, name='movies'),
    path('subscriber/movie-info/<int:passed_id>/', views.movie_info, name='movie_info'),
    path('subscriber/movie-part/<int:movie_part_id>/', views.movie_part_details, name='movie_part_details'),
    path('subscriber/favourites/', views.favourites, name='favourites'),
]
