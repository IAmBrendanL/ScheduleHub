import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from django.forms.models import fields_for_model
from .widget import DateTime
from .models import AvailableTime, ScheduleHubGroup, group_name_regex_val


class RegisterForm(UserCreationForm):
    """
    Extends the UCF to add extra fields
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class TimeFixField(forms.MultiValueField):
    widget = DateTime

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
        )
        super(TimeFixField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return data_list[0] + ':' + data_list[1] + ' ' + data_list[2]
        return None


class GetStartAndEndDatesForm(forms.ModelForm):
    """
    Gets data from the user
    """
    start_date = forms.DateField(widget=SelectDateWidget, initial=datetime.date.today())
    start_time = TimeFixField(widget=DateTime)
    end_date = forms.DateField(widget=SelectDateWidget, initial=datetime.date.today())
    end_time = TimeFixField(widget=DateTime)

    class Meta:
        model = AvailableTime
        fields = ('start_date', 'start_time', 'end_date', 'end_time')


class AddGroupForm(forms.Form):
    """
    Form for adding new groups
    """
    name = forms.CharField(required=True, validators=[group_name_regex_val])
    name.widget.attrs['class'] = 'form-control'
    _model_fields = fields_for_model(ScheduleHubGroup, fields=['users'])
    users = _model_fields['users']
    users.widget.attrs['class'] = 'form-control'


