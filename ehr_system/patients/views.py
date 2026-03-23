from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect,get_list_or_404
from .forms import PatientForm
from .models import Patient
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.contrib import messages


def add_patient(request):
    form=PatientForm()
    if request.method=="POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request,'add_patient.html',{'form':form})

@login_required
def view_patients(request):
    patients=Patient.objects.all()
    return render(request,'view_patients.html',{'patients':patients})

@login_required
def edit_patient(request,id) -> HttpResponseRedirect | HttpResponse:
    patient=get_object_or_404(Patient,id=id)
    form=PatientForm(instance=patient)

    if request.method=="POST":
        form=PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect("view_patients")
    return render(request,'add_patient.html',{'form':form})

@login_required
def delete_patient(request,id) -> HttpResponseRedirect:
    patient=get_object_or_404(Patient,id=id)
    patient.delete()
    return redirect("view_patients")


#  LOGIN VIEW
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('view_patients')  # after login
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')


#  REGISTER VIEW


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

    #check passwords match
        if password != confirm_password:
            return render(request, 'register.html', {
                'error': 'Passwords do not match'
            })

        # check user exists
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        # create user
        user = User.objects.create_user(username=username, password=password)

        #  auto login
        login(request, user)
        return redirect('view_patients')
    return render(request, 'register.html')


# 🚪 LOGOUT
def user_logout(request):
    logout(request)
    return redirect('login')

