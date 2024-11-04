from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

class ServiceForm(ModelForm):
    class Meta:
        model = Services
        fields = '__all__'

class DoctorListForm(ModelForm):
    class Meta:
        model = DoctorList
        fields = '__all__'

class ICUForm(ModelForm):
    class Meta:
        model = ICUVacancy
        fields = '__all__'

class AmbulanceForm(ModelForm):
    class Meta:
        model = Ambulance
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


