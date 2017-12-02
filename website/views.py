from django.shortcuts import render, redirect
from .models import AvailableTime, ScheduleHubGroup
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, GetStartAndEndDatesForm, AddGroupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
import datetime


# Create your views here.

def index(request):
    """
    View for welcome page of website
    """
    return render(request, 'index.html')


class AvailabilityListView(LoginRequiredMixin, generic.ListView):
    """
    View for showing user availability
    Requires auth
    """
    # properties
    model = AvailableTime
    template_name = 'available_time.html'
    paginate_by = 10

    # methods
    def get_queryset(self):
        # get all instances that relate to the user who made the request
        return AvailableTime.objects.filter(user=self.request.user)


class GroupListView(LoginRequiredMixin, generic.ListView):
    """
    View for showing all groups
    Requires auth
    """
    # properties
    model = ScheduleHubGroup
    template_name = "group_list.html"
    paginate_by = 10

    # methods
    def get_queryset(self):
        # get all instances of groups
        return ScheduleHubGroup.objects.all()


@login_required
def addGroupView(request):
    """
    View for adding new groups
    """
    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            return redirect('/website/groups/')
        else:
            return render(request, 'add_group.html', {'form': form})
    else:
        return render(request, 'add_group.html', {'form': AddGroupForm()})


@login_required
def getAvailableTime(request):
    """
    if request.method == 'POST':
    """
    if request.method == 'POST':
        form = GetStartAndEndDatesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # get date time
            startTime = datetime.datetime.strptime(data['start_time'], '%I:%M %p').time()
            endTime = datetime.datetime.strptime(data['end_time'], '%I:%M %p').time()
            startDateTime = datetime.datetime.combine(data['start_date'], startTime)
            endDateTime = datetime.datetime.combine(data['end_date'], endTime)
            # check valid date time and return appropriate page
            if startDateTime >= endDateTime:
                # if not valid return same form and set error
                messages.error(request, "Please enter a interval of time that is greater than 0.")
                return render(request, 'add_availability.html', {'form': form})
            else:
                AvailableTime.objects.create(startTime=startDateTime, endTime=endDateTime, user=request.user)
                return redirect('/website/my-time/')
        else:
            print('form was not valid')
            return render(request, 'add_availability.html', {'form': GetStartAndEndDatesForm()})
    else:
        return render(request, 'add_availability.html', {'form': GetStartAndEndDatesForm()})


def registerUser(request):
    """
    View for registering new users
    """
    if request.method == 'POST':
        # if good, set up user form and get data
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('my-time')
        else:
            return render(request, 'register.html', {'form': RegisterForm()})
    else:
        # else, set up user form and try again
        return render(request, 'register.html', {'form': RegisterForm()})
