from django.contrib import admin
from .models import Location, Hospital, Ambulance,ICUVacancy, Services, DoctorList

# Register your models here.
admin.site.register([Location,Hospital,Ambulance,ICUVacancy,Services,DoctorList])