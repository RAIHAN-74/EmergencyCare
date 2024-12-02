"""
URL configuration for emcsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, paths
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from emergencycare import views as e_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',e_views.Homepage, name = 'Home'),
    path('register/',e_views.registerPage,name='register'),
    path('login/',e_views.loginPage,name='login'),
    path('logout/',e_views.logoutUser,name='logout'),
    path('admin/', admin.site.urls),
	path('search',e_views.search,name='search'),
    path('Users/',e_views.users,name='Users'),
	path('Hospital/',e_views.hospital,name='hospital'),
    path('add_hospital/',e_views.add_hospital,name='add_hospital'),
    path('Hospital/<str:id>',e_views.details, name='Details'),
    path('update_hospital/<str:id>',e_views.update_hospital,name='update_hospital'),
    path('delete_hospital/<str:id>',e_views.delete_hospital,name='delete_hospital'),
	path('Services/',e_views.services,name='Services'),
    path('add_service/',e_views.add_service,name='add_service'),
    path('update_service/<str:id>',e_views.update_service,name='update_service'),
    path('delete_service/<str:id>',e_views.delete_service,name='delete_service'),
	path('Ambulance/',e_views.ambulance,name='Ambulance'),
    path('add_ambulance/',e_views.add_ambulance,name='add_ambulance'),
    path('update_ambulance/<str:id>',e_views.update_ambulance,name='update_ambulance'),
    path('delete_ambulance/<str:id>',e_views.delete_ambulance,name='delete_ambulance'),
	path('ICUVacancy/',e_views.icuvac,name='ICUVacancy'),
	path('DoctorList/',e_views.doctorlist,name='DoctorList'),
    path('add_doctor/',e_views.add_doctor,name='add_doctor'),
    path('update_doctor/<str:id>',e_views.update_doctor,name='update_doctor'),
    path('delete_doctor/<str:id>',e_views.delete_doctor,name='delete_doctor'),
    path('add_ICU/',e_views.add_ICU,name='add_ICU'),
    path('update_ICU/<str:id>',e_views.update_ICU,name='update_ICU'),
    path('delete_ICU/<str:id>',e_views.delete_ICU,name='delete_ICU'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)