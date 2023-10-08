from django.contrib import admin

from . import models
# Register your models here.
admin.site.register([
    models.FavouriteMovie,
    models.FavouriteSeries,
    models.WatchlistMoviesPart,
    models.WatchlistSeason,
    models.ContinueWatchingMoviePart,
    models.ContinueWatchingEpisodes,
    models.ShowRatingMoviePart,
    models.ShowRatingEpisodes,
    models.BestCollection,
    models.ShowCollectionMovie,
    models.ShowCollectionSeries,
])