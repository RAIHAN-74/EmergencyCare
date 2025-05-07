from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.models import User


# Register your models here
admin.site.register([Location, Hospital, Ambulance, ICUVacancy, Services, DoctorList, CCU, NICU, NICUBooking, CCUBooking, ICUBooking, ServiceDetail])


# Inline admin for the Profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


class CustomUserAdmin(UserAdmin):
    def get_area_name(self, obj):
        return obj.profile.Area_name if obj.profile.Area_name else 'No Location'

    get_area_name.short_description = 'Area Name'

    list_display = UserAdmin.list_display + ('get_area_name',)

    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
