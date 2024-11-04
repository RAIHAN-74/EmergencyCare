from django.shortcuts import render,redirect

from emcsystem.decorators import unauthenticated_user
from .forms import *
from .models import Location,Hospital,User,Ambulance,ICUVacancy,DoctorList,Services

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
def Homepage(request):
    return render(request, template_name='Home.html')

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name = 'User')
            user.groups.add(group)

            messages.success(request, message='Account was created for ' + username)

            return redirect('login')

    context = {
         'form': form
        }
    return render(request, template_name='Register.html', context=context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.info(request, message="Username or password is incorrect")

    context = {}
    return render(request, template_name='Login.html', context=context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def location(request):
    return render(request,template_name='Home.html')
def search(request):
    if request.method == "POST":
        keyword = request.POST.get('Search')
        if keyword.lower() == "hospital":
            return redirect('Hospital/')
        elif keyword.lower() == "services":
            return redirect('Services/')
        elif keyword.lower() == "doctor":
            return redirect('DoctorList/')
        elif keyword.lower() == "ambulance":
            return redirect('Ambulance/')
        elif keyword.lower() == "icu":
            return redirect('ICUVacancy/')

    return render(request,template_name='Home.html')

@login_required(login_url='login')
def hospital(request):
    hospital = Hospital.objects.all()
    context={
       'hospital':hospital,
    }
    return render(request,template_name='hospital.html',context=context)

@login_required(login_url='login')
def services(request):
    service = Services.objects.all()
    context = {
        'service': service,
    }
    return render(request, template_name='Services.html',context=context)


@login_required(login_url='login')
def ambulance(request):
    ambulance = Ambulance.objects.all()
    context = {
        'ambulance': ambulance,
    }
    return render(request, template_name='Ambulance.html',context=context)

@login_required(login_url='login')
def icuvac(request):
    icuvac = ICUVacancy.objects.all()
    context = {
        'icuvac': icuvac,
    }
    return render(request, template_name='ICUVacancy.html',context=context)

@login_required(login_url='login')
def doctorlist(request):
    doctorlist = DoctorList.objects.all()
    context = {
        'doctorlist': doctorlist,
    }
    return render(request, 'DoctorList.html', context=context)


