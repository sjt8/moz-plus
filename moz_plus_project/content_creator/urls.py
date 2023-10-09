from django.urls import path
from .views import add_movie,edit_movie,add_series,edit_series,delete_movie,delete_series,delete_Season,delete_episode
from . import views
app_name = 'content_creator'

urlpatterns = [
    path("add_movie/",add_movie, name='add_movie'),
    path("edit-movie/<int:passed_id>/",edit_movie, name='edit_movie'),
    path('add-series/',add_series, name='add_series'),
    path("edit-series/<int:passed_id>/",edit_series, name='edit_series'),
    path("delete_movie/<int:passed_id>/",delete_movie, name='delete_movie'),
    path("delete_series/<int:passed_id>/",delete_series, name='delete_series'),
    path("delete_series/<int:passed_id>/",delete_Season, name='delete_season'),
    path("delete_series/<int:passed_id>/",delete_episode, name='delete_episode'),
    path('series/<int:passed_id>/', views.series_list, name='view_series'),

]
