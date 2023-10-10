from django.urls import path

from . import views

app_name = 'content_creator'

urlpatterns = [
    path('content-creator/', views.content_creator, name='content_creator'),
    path('content-creator/series/', views.series, name='series'),
    path('content-creator/series/<int:series_id>/', views.series_details, name='series_details'),
]
