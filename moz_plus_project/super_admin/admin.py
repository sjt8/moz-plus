from django.contrib import admin

from . import models
# Register your models here.

admin.site.register([
    models.Country,
    models.Language,
    models.ContentRating,
    models.Genre,
    models.ShowRole,
    models.Studio,
    models.SubscriptionPlan,
])