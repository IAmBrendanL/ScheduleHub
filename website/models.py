from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class AvailableTime(models.Model):
    """
    A model that represents available times for a user or group
    """
    # properties (fields)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    # relationships defined in the user and group models
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    # meta
    class Meta:
        # order by startTime then endTime in normal order
        ordering = ["startTime", "endTime"]

    def __str__(self):
        return self.startTime.strftime('%I:%M %p |  %m/%d/%y ') + " to " + self.endTime.strftime('%I:%M %p |  %m/%d/%y ')


class ScheduleHubGroup(models.Model):
    """
    A model that represents a group of users
    """
    # properties (fields)
    name = models.CharField(max_length=128, help_text="Enter a name")

    # relationships
    times = models.ForeignKey(AvailableTime, on_delete=models.SET_NULL, null=True)
    users = models.ManyToManyField(User)

    # meta
    class Meta:
        # order by name
        ordering = ["name"]

    # Methods
    # def get_absolute_url(self):
    #     return reverse('scheduleHub')

    def __str__(self):
        return self.name

