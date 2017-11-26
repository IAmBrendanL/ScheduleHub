from django.shortcuts import render, redirect
from .models import AvailableTime, User, ScheduleHubGroup
from django.contrib.auth import authenticate, login, logout
from .forms import registerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.

def index(request):
    """
    View for welcome page of website
    """
    return render(request, 'index.html')

class AvailabilityListView(LoginRequiredMixin, generic.ListView):
    """
    View for user adding availability
    """
    """
    okay, what do I need?
    I need to be able to add time 
    """
    model =  AvailableTime
    template_name = 'available_time.html'
    paginate_by = 10

    def get_queryset(self):
        return AvailableTime.objects.filter(user=self.request.user)




def registerUser(request):
    """
    View for registering new users
    """
    if request.method == 'POST':
        # if good, set up user form and get data
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data.get('username')
            userPassword = form.cleaned_data.get('password')
            user = authenticate(username=userName, password=userPassword)
            login(request,user)
            return render(redirect(AvailabilityListView))
    else:
        # else, set up user form and try again
        form = registerForm()
        return render(request, 'register.html', {'form': form})


def loginUser(request):
    """
    View for logging users in
    """


def logoutUser(request):
    """
    View for logging users out
    """
    logout(request)
    # return a success logout page
