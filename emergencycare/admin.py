from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Location,Hospital,Ambulance,ICUVacancy,Services,DoctorList,CCU,NICU,NICUBooking,CCUBooking,ICUBooking,ServiceDetail])