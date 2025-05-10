from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    Area_name = models.CharField(max_length=200)
    Location_Number = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.Area_name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Area_name = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
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
    Contact_Number = models.CharField(max_length=15,null=True,blank=True,)
    def __str__(self):
        return self.A_Number
class ICUVacancy(models.Model):
    H_Name = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    Number_of_ICU = models.IntegerField(blank=True, null=True)
    ICU_Budget = models.IntegerField(blank=True, null=True)
    Vacant = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.Vacant)
class ICUBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.patient_name}"
class CCU(models.Model):
    H_Name = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    Number_of_CCU = models.IntegerField(blank=True, null=True)
    CCU_Budget = models.IntegerField(blank=True, null=True)
    Vacant = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.Vacant)


class CCUBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    CONDITION_CHOICES = [
        ('stable', 'Stable'),
        ('bad', 'Bad'),
        ('critical', 'Critical'),
        ('emergency', 'Emergency'),
    ]

    patient_condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default='stable'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name}"


class NICU(models.Model):
    H_Name = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    Number_of_NICU = models.IntegerField(blank=True, null=True)
    NICU_Budget = models.IntegerField(blank=True, null=True)
    Vacant = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.Vacant)

class NICUBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guardian_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    baby_name = models.CharField(max_length=100,null=True,blank=True)
    baby_age = models.CharField(max_length=50, blank=True, null=True)
    CONDITION_CHOICES = [
        ('stable', 'Stable'),
        ('bad', 'Bad'),
        ('critical', 'Critical'),
        ('emergency', 'Emergency'),
    ]
    baby_condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default='stable'
    )
    requirements = models.CharField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guardian_name}"
class Services(models.Model):
    H_Name = models.ForeignKey(Hospital, on_delete=models.CASCADE, blank=True, null=True)
    S_ID = models.CharField(max_length=200, blank=True, null=True)
    S_Name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.S_Name
class ServiceDetail(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='details')
    type = models.CharField(max_length=50)
    intensity = models.CharField(max_length=50)
    estimated_budget = models.IntegerField()

    def __str__(self):
        return f"{self.service.S_Name}"


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