import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .widget import DateTime
from .models import User, AvailableTime


class registerForm(UserCreationForm):
    """
    Extends the UCF to add extra fields
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class getStartAndEndDatesForm(forms.ModelForm):
    """
    Gets data from the user
    """
    start_date = forms.DateField(widget=SelectDateWidget, initial=datetime.date.today())
    start_time = forms.MultipleChoiceField(widget=DateTime)
    end_date = forms.DateField(widget=SelectDateWidget, initial=datetime.date.today())
    end_time = forms.MultipleChoiceField(widget=DateTime)

    class Meta:
        model = AvailableTime
        fields = ('start_date', 'start_time', 'end_date', 'end_time')
