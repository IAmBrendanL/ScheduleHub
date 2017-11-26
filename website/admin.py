from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import AvailableTime, User, ScheduleHubGroup

# Register your models here.
admin.site.register(AvailableTime)
admin.site.register(ScheduleHubGroup)
admin.site.register(User, UserAdmin)
