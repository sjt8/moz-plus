from django.urls import path
from .views import add_season,add_episode,edit_season,delete_Season,delete_episode,add_series,edit_episode
from . import views

app_name = 'content_creator'

urlpatterns = [
    path('content-creator/', views.content_creator, name='content_creator'),
    path('content-creator/series/', views.series, name='series'),
    path('content-creator/series/<int:series_id>/', views.series_details, name='series_details'),
    path('add-season/',add_season, name='add_season'),
    path('add-episode/',add_episode, name='add_episode'),
    path("edit-season/<int:passed_id>/",edit_season, name='edit_season'),
    path("delete_season/<int:season_id>/", delete_Season, name='delete_season'),
    path("delete_episode/<int:episode_id>/", delete_episode, name='delete_episode'),
    path('add-series/',add_series, name='add_series'),
    path("edit-episode/<int:passed_id>/", edit_episode, name='edit_episode'),

]
