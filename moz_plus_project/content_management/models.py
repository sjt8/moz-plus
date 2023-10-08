from django.db import models

# Create your models here.

RATINGS = (
    (1, 1.0),
    (2, 1.5),
    (3, 2.0),
    (4, 2.5),
    (5, 3.0),
    (6, 3.5),
    (7, 4.0),
    (8, 4.5),
    (9, 5.0),
)


class FavouriteMovie(models.Model):
    subscriber = models.ForeignKey('subscriber.Subscriber', on_delete=models.CASCADE)
    movie_part = models.ForeignKey('content_creator.MoviePart', on_delete=models.CASCADE, null=True)


class FavouriteSeries(models.Model):
    subscriber = models.ForeignKey('subscriber.Subscriber', on_delete=models.CASCADE)
    series = models.ForeignKey('content_creator.Series', on_delete=models.CASCADE, null=True)


class WatchlistMoviesPart(models.Model):
    subscriber = models.ForeignKey('subscriber.Subscriber', on_delete=models.CASCADE)
    movie_part = models.ForeignKey('content_creator.MoviePart', on_delete=models.CASCADE, null=True)


class WatchlistSeason(models.Model):
    subscriber = models.ForeignKey('subscriber.Subscriber', on_delete=models.CASCADE)
    season = models.ForeignKey('content_creator.Season', on_delete=models.CASCADE, null=True)


class ContinueWatchingMoviePart(models.Model):
    subscriber = models.ForeignKey('subscriber.Subscriber', on_delete=models.CASCADE)
    movie_part = models.ForeignKey('content_creator.MoviePart', on_delete=models.CASCADE, null=True)
    watch_duration = models.DurationField()

    def __str__(self):
        return f'{self.movie_part.title}: {self.watch_duration}'


class ContinueWatchingEpisodes(models.Model):
    subscriber = models.ForeignKey('subscriber.Subscriber', on_delete=models.CASCADE)
    episodes = models.ForeignKey('content_creator.Episodes', on_delete=models.CASCADE, null=True)
    watch_duration = models.DurationField()

    def __str__(self):
        return f'{self.episodes.title}: {self.watch_duration}'


class ShowRatingMoviePart(models.Model):
    subscriber = models.ForeignKey('subscriber.Subscriber', on_delete=models.CASCADE)
    movie_part = models.ForeignKey('content_creator.MoviePart', on_delete=models.CASCADE, null=True)
    rating = models.PositiveSmallIntegerField(choices=RATINGS, default=1)


class ShowRatingEpisodes(models.Model):
    subscriber = models.ForeignKey('subscriber.Subscriber', on_delete=models.CASCADE)
    episodes = models.ForeignKey('content_creator.Episodes', on_delete=models.CASCADE, null=True)
    rating = models.PositiveSmallIntegerField(choices=RATINGS, default=1)


class BestCollection(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.title


class ShowCollectionMovie(models.Model):
    best_collection = models.ForeignKey(BestCollection, on_delete=models.CASCADE)
    movie = models.ForeignKey('content_creator.Movie', on_delete=models.CASCADE, null=True)


class ShowCollectionSeries(models.Model):
    best_collection = models.ForeignKey(BestCollection, on_delete=models.CASCADE)
    series = models.ForeignKey('content_creator.Series', on_delete=models.CASCADE, null=True)
