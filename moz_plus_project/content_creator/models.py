from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class ContentCreator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    phone_no = models.CharField(max_length=20, unique=True)
    country = models.ForeignKey('super_admin.Country', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='content_creator/profile/images')
    about = models.TextField(max_length=1000)
    studio = models.ManyToManyField('super_admin.Studio')
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class ShowPerson(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    dob = models.DateField()
    country = models.ForeignKey('super_admin.Country', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='content_creator/show_person/profile/images')
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name}'


class ShowPersonRole(models.Model):
    show_person = models.ForeignKey(ShowPerson, on_delete=models.CASCADE)
    role = models.ForeignKey('super_admin.ShowRole', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.show_person.first_name} {self.role.name}'


class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    overview = models.TextField(max_length=500)
    is_enable = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='content_creator/movies/images')

    def __str__(self):
        return self.title


class Series(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    overview = models.TextField(max_length=500)
    genre = models.ManyToManyField('super_admin.Genre')
    country = models.ManyToManyField('super_admin.Country')
    is_enable = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='content_creator/series/images')

    def __str__(self):
        return self.title


class MoviePart(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    studio = models.ForeignKey('super_admin.Studio', on_delete=models.CASCADE)
    part_no = models.PositiveSmallIntegerField()
    genre = models.ManyToManyField('super_admin.Genre')
    plot = models.TextField(max_length=500)
    person = models.ManyToManyField(ShowPersonRole)
    release_date = models.DateField()
    duration = models.DurationField()
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    content_rating = models.ForeignKey('super_admin.ContentRating', on_delete=models.SET_DEFAULT,
                                       default=1)
    country = models.ForeignKey('super_admin.Country', on_delete=models.CASCADE)
    language = models.ManyToManyField('super_admin.Language')
    is_enable = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='content_creator/movies_part/images')
    video = models.FileField(upload_to='content_creator/movies_part/videos')

    def __str__(self):
        return self.slug


class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    season_no = models.PositiveSmallIntegerField()
    overview = models.TextField(max_length=500, blank=True)
    studio = models.ManyToManyField('super_admin.Studio')
    language = models.ManyToManyField('super_admin.Language')
    release_date = models.DateTimeField()
    thumbnail = models.ImageField(upload_to='content_creator/season/images')
    is_enable = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.series.title} - {self.season_no}'


class Episodes(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    episode_no = models.PositiveSmallIntegerField()
    plot = models.TextField(max_length=500)
    person = models.ManyToManyField(ShowPersonRole)
    release_date = models.DateField()
    duration = models.DurationField()
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    content_rating = models.ForeignKey('super_admin.ContentRating', on_delete=models.SET_DEFAULT,
                                       default=1)
    is_enable = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='content_creator/episode/images')
    video = models.FileField(upload_to='content_creator/episode/videos')

    def __str__(self):
        return self.slug


class ContentMovie(models.Model):
    creator = models.ForeignKey(ContentCreator, on_delete=models.CASCADE)
    movie = models.ForeignKey(MoviePart, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.creator.user.username}: {self.movie.title}'


class ContentSeries(models.Model):
    creator = models.ForeignKey(ContentCreator, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.creator.user.username}: {self.series.title}'


class MovieTrailer(models.Model):
    movie_part = models.ForeignKey(MoviePart, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f'M{self.movie_part.movie.title}: {self.movie_part.part_no}'


class SeasonTrailer(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f'S{self.season.series.title}: {self.season.season_no}'
