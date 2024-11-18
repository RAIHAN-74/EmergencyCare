from django.shortcuts import render,redirect

from emcsystem.decorators import unauthenticated_user,allowed_user,admin_only
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
def users(request):
    return render(request,template_name='Users.html')
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'Users.html')
    else:
        return redirect('Home.html')
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
        elif keyword.lower() == "doctorlist":
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
def details(request, id):
    hospital = Hospital.objects.get(pk=id)
    icuvac = ICUVacancy.objects.filter(H_Name=id)
    services = Services.objects.filter(H_Name=id)
    doctorlist = DoctorList.objects.filter(H_Name=id)

    context = {
        'hospital': hospital,
        'icuvac': icuvac,
        'services': services,
        'doctorlist':doctorlist

    }
    return render(request, template_name='Details.html', context=context)


@allowed_user(allowed_roles=['Admin'])
def add_hospital(request):
    form = HospitalForm()
    if request.method == 'POST':
        form = HospitalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hospital')

    context = {
        'form':form
    }
    return render(request, template_name='add_hospital.html',context=context)

@allowed_user(allowed_roles=['Admin'])
def update_hospital(request, id):
    hospital = Hospital.objects.get(pk = id)
    form = HospitalForm(instance=hospital)
    if request.method == 'POST':
        form = HospitalForm(request.POST, request.FILES, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital')

    context = {'form':form}
    return render(request, template_name='add_hospital.html', context=context)

@allowed_user(allowed_roles=['Admin'])
def delete_hospital(request, id):
    hospital = Hospital.objects.get(pk = id)
    if request.method == 'POST':
        hospital.delete()
        return redirect('hospital')

    return render(request, template_name='delete_hospital.html')


@login_required(login_url='login')
def services(request):
    service = Services.objects.all()
    context = {
        'service': service,
    }
    return render(request, template_name='Services.html',context=context)
@allowed_user(allowed_roles=['Admin'])
def add_service(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Services')

    context = {
        'form':form
    }
    return render(request, template_name='add_service.html',context=context)

@allowed_user(allowed_roles=['Admin'])
def update_service(request, id):
    services = Services.objects.get(pk = id)
    form = ServiceForm(instance=services)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=services)
        if form.is_valid():
            form.save()
            return redirect('Services')

    context = {'form':form}
    return render(request, template_name='add_service.html', context=context)

@allowed_user(allowed_roles=['Admin'])
def delete_service(request, id):
    services = Services.objects.get(pk = id)
    if request.method == 'POST':
        services.delete()
        return redirect('Services')

    return render(request, template_name='delete_service.html')

@login_required(login_url='login')
def ambulance(request):
    ambulance = Ambulance.objects.all()
    context = {
        'ambulance': ambulance,
    }
    return render(request, template_name='Ambulance.html',context=context)
@allowed_user(allowed_roles=['Admin'])
def add_ambulance(request):
    form = AmbulanceForm()
    if request.method == 'POST':
        form = AmbulanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Ambulance')

    context = {
        'form':form
    }
    return render(request, template_name='add_ambulance.html',context=context)
@allowed_user(allowed_roles=['Admin'])
def update_ambulance(request, id):
    ambulance = Ambulance.objects.get(pk = id)
    form = AmbulanceForm(instance=ambulance)
    if request.method == 'POST':
        form = AmbulanceForm(request.POST, request.FILES, instance=ambulance)
        if form.is_valid():
            form.save()
            return redirect('Ambulance')

    context = {'form':form}
    return render(request, template_name='add_ambulance.html', context=context)

@allowed_user(allowed_roles=['Admin'])
def delete_ambulance(request, id):
    ambulance = Ambulance.objects.get(pk = id)
    if request.method == 'POST':
        ambulance.delete()
        return redirect('Ambulance')

    return render(request, template_name='delete_ambulance.html')

@login_required(login_url='login')
def icuvac(request):
    icuvac = ICUVacancy.objects.all()
    context = {
        'icuvac': icuvac,
    }
    return render(request, template_name='ICUVacancy.html',context=context)
@allowed_user(allowed_roles=['Admin'])
def add_ICU(request):
    form = ICUForm()
    if request.method == 'POST':
        form = ICUForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ICUVacancy')

    context = {
        'form':form
    }
    return render(request, template_name='add_ICU.html',context=context)
@allowed_user(allowed_roles=['Admin'])
def update_ICU(request, id):
    icuvac = ICUVacancy.objects.get(pk = id)
    form = ICUForm(instance=icuvac)
    if request.method == 'POST':
        form = ICUForm(request.POST, request.FILES, instance=icuvac)
        if form.is_valid():
            form.save()
            return redirect('ICUVacancy')

    context = {'form':form}
    return render(request, template_name='add_ICU.html', context=context)

@allowed_user(allowed_roles=['Admin'])
def delete_ICU(request, id):
    icuvac = ICUVacancy.objects.get(pk = id)
    if request.method == 'POST':
        icuvac.delete()
        return redirect('ICUVacancy')

    return render(request, template_name='delete_ICU.html')

@login_required(login_url='login')
def doctorlist(request):
    doctorlist = DoctorList.objects.all()
    context = {
        'doctorlist': doctorlist,
    }
    return render(request, 'DoctorList.html', context=context)

@allowed_user(allowed_roles=['Admin'])
def add_doctor(request):
    form = DoctorListForm()
    if request.method == 'POST':
        form = DoctorListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('DoctorList')

    context = {
        'form':form
    }
    return render(request, template_name='add_doctor.html',context=context)

@allowed_user(allowed_roles=['Admin'])
def update_doctor(request, id):
    doctorlist = DoctorList.objects.get(pk = id)
    form = DoctorListForm(instance=doctorlist)
    if request.method == 'POST':
        form = DoctorListForm(request.POST, request.FILES, instance=doctorlist)
        if form.is_valid():
            form.save()
            return redirect('DoctorList')

    context = {'form':form}
    return render(request, template_name='add_doctor.html', context=context)

@allowed_user(allowed_roles=['Admin'])
def delete_doctor(request, id):
    doctorlist = DoctorList.objects.get(pk = id)
    if request.method == 'POST':
        doctorlist.delete()
        return redirect('DoctorList')

    return render(request, template_name='delete_doctor.html')

