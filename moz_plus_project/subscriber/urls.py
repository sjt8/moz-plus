from django.urls import path

from . import views

app_name = 'subscriber'

urlpatterns = [
    path('subscriber/', views.subscriber, name='subscriber'),
    path('subscriber/series/', views.series, name='series'),
    path('subscriber/series/<int:series_id>/', views.series_details, name='series_details'),
]
