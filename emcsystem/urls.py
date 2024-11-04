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
	path('Hospital/',e_views.hospital,name='hospital'),
	path('Services/',e_views.services,name='Services'),
	path('Ambulance/',e_views.ambulance,name='Ambulance'),
	path('ICUVacancy/',e_views.icuvac,name='ICUVacancy'),
	path('DoctorList/',e_views.doctorlist,name='DoctorList'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)