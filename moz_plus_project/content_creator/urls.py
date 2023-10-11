from django.urls import path
from .views import add_season,add_episode,edit_season,delete_Season,delete_episode,add_series,edit_episode
from . import views

app_name = 'content_creator'

urlpatterns = [
    path('content-creator/', views.content_creator, name='content_creator'),
    path('content-creator/series/', views.series, name='series'),
    path('content-creator/movies/', views.movies, name='movies'),
    path('content-creator/series/<int:series_id>/', views.series_details, name='series_details'),
    path('content-creator/add-season/',add_season, name='add_season'),
    path('content-creator/add-episode/',add_episode, name='add_episode'),
    path("content-creator/edit-season/<int:passed_id>/",edit_season, name='edit_season'),
    path("content-creator/delete_season/<int:season_id>/", delete_Season, name='delete_season'),
    path("content-creator/delete_episode/<int:episode_id>/", delete_episode, name='delete_episode'),
    path('content-creator/add-series/',add_series, name='add_series'),
    path("content-creator/edit-episode/<int:passed_id>/", edit_episode, name='edit_episode'),

]
