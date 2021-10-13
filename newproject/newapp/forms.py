from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Ambulancemodel,Drformmodel,Nursingmodel,Roomservicemodel

ch=[('Yes','Yes'),
         ('No','No')]
slo=[('Afternoon_slot','Afternoon_slot'),('Evening_slot','Evening_slot')]

gen=(('male','male'),('famale','female'))


class Userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1']


class Ambulaceform(forms.ModelForm):
    class Meta:
        model=Ambulancemodel
        fields="__all__"

class Dateinput(forms.DateInput):
    input_type='date'


class Appointmentform(forms.Form):
    name = forms.CharField(max_length=30)
    gender = forms.ChoiceField(choices=gen)
    city = forms.CharField(max_length=30)
    Have_you_previously_attended_facility = forms.ChoiceField(choices=ch, widget=forms.RadioSelect)
    if_yes_state_on_which_condition_and_when = forms.CharField(max_length=40)
    please_select_appointment_date=forms.DateField(widget=Dateinput)
    slot = forms.ChoiceField(choices=slo, widget=forms.RadioSelect)

class Doctorform(forms.ModelForm):
    class Meta:
        model=Drformmodel
        fields="__all__"

class Nursingform(forms.ModelForm):
    class Meta:
        model=Nursingmodel
        fields="__all__"

class Roomserviceform(forms.ModelForm):
    class Meta:
        model=Roomservicemodel
        fields="__all__"
