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
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Location, Profile

class CreateUserForm(UserCreationForm):
    location = forms.ModelChoiceField(queryset=Location.objects.all(), required=True, label="Area Name")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        # Save the user first
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create the Profile and associate the selected Location
            profile = Profile.objects.create(user=user, Area_name=self.cleaned_data['location'])
        return user


class ICUBookingForm(forms.ModelForm):
    class Meta:
        model = ICUBooking
        fields = ['patient_name', 'contact' ]

class NICUBookingForm(forms.ModelForm):
    class Meta:
        model = NICUBooking
        fields = ['guardian_name', 'contact','baby_name' ,'baby_condition', 'requirements' ]
class CCUBookingForm(forms.ModelForm):
    class Meta:
        model = CCUBooking
        fields = ['patient_name', 'contact', 'patient_condition']




