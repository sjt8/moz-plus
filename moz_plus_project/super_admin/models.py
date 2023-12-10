from django.db import models


# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ContentRating(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ShowRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="super_admin/studio/images")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=3, decimal_places=2)
    months = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
