from django.contrib import admin

from . import models

# Register your models here.
admin.site.register([
    models.ContentCreator,
    models.ShowPerson,
    models.ShowPersonRole,
    models.Movie,
    models.Series,
    models.MovieTrailer,
    models.SeasonTrailer,
    models.MoviePart,
    models.Season,
    models.Episodes,
])
