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


class timeFixField(forms.MultiValueField):
    widget = DateTime

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
        )
        super(timeFixField, self).__init__(fields,*args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return data_list[0] + ':' + data_list[1] + ' ' + data_list[2]
        return None




class getStartAndEndDatesForm(forms.ModelForm):
    """
    Gets data from the user
    """
    start_date = forms.DateField(widget=SelectDateWidget, initial=datetime.date.today())
    start_time = timeFixField(widget=DateTime)
    end_date = forms.DateField(widget=SelectDateWidget, initial=datetime.date.today())
    end_time = timeFixField(widget=DateTime)

    class Meta:
        model = AvailableTime
        fields = ('start_date', 'start_time', 'end_date', 'end_time')
