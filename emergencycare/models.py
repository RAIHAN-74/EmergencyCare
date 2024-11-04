from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    Area_name = models.CharField(max_length=200)
    def __str__(self):
        return self.Area_name

class Hospital(models.Model):
    H_ID = models.CharField(max_length=200)
    H_name = models.CharField(max_length=200)
    Area_name = models.ForeignKey(Location, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='images/',blank=True, null=True, default='images/default.jpg')

    def __str__(self):
        return self.H_name

class Ambulance(models.Model):
    Area_name = models.ForeignKey(Location, on_delete=models.CASCADE)
    A_Number = models.CharField(max_length=200)
    def __str__(self):
        return self.A_Number
class ICUVacancy(models.Model):
    H_Name = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    Number_of_ICU = models.IntegerField(blank=True, null=True)
    ICU_Budget = models.IntegerField(blank=True, null=True)
    Vacant = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.Vacant
class Services(models.Model):
    H_Name = models.ForeignKey(Hospital, on_delete=models.CASCADE, blank=True, null=True)
    S_ID = models.CharField(max_length=200, blank=True, null=True)
    S_Name = models.CharField(max_length=200, blank=True, null=True)
    S_Budget = models.IntegerField(blank=True, null=True)

    image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/default.jpg')
    def __str__(self):
        return self.S_Name

class DoctorList(models.Model):
    H_Name = models.ForeignKey(Hospital, on_delete=models.CASCADE, blank=True, null=True)
    D_ID = models.CharField(max_length=200, blank=True, null=True)
    D_Name = models.CharField(max_length=200, blank=True, null=True)
    D_Experience = models.CharField(max_length=200, blank=True, null=True)
    D_Speciality = models.CharField(max_length=200, blank=True, null=True)
    status_availabilty = (
       ('Available','Available'),
        ('Not Available', 'Not Available'),
    )
    Availability = models.CharField(max_length=100, choices=status_availabilty,blank=True,null=True)

    image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/default.jpg')

    def __str__(self):
        return self.D_Name