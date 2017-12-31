from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Validators
# Regex validator for groups
group_name_regex_val = RegexValidator(r'^[0-9a-zA-Z _-]*$', "A group name can only contain alphanumeric characters, "
                                                            "spaces, hyphens, and underscores")

# Models
class AvailableTime(models.Model):
    """
    A model that represents available times for a user or group
    """
    # properties (fields)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    # has a many to one relation to a django user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

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
    name = models.CharField(max_length=128, validators=[group_name_regex_val])

    # relationships
    times = models.ForeignKey(AvailableTime, on_delete=models.SET_NULL, null=True)
    users = models.ManyToManyField(User, help_text="Hold down ctrl (or cmd on a Mac) to select multiple")

    # meta
    class Meta:
        # order by name
        ordering = ["name"]

    # Methods
    # def get_absolute_url(self):
    #     return reverse('scheduleHub')

    def __str__(self):
        return self.name


