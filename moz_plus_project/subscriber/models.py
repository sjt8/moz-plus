from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    phone_no = models.CharField(max_length=20, unique=True)
    country = models.ForeignKey("super_admin.Country", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subscriber/profile/images')
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Subscription(models.Model):
    subscriber = models.OneToOneField(Subscriber, on_delete=models.CASCADE)
    plan = models.ForeignKey("super_admin.SubscriptionPlan", on_delete=models.CASCADE, null=True,
                             default=1)
    last_subscription = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subscriber.user.username} : {self.plan.name}'
