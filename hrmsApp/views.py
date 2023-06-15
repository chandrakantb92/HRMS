from django.http import HttpResponse
from django.shortcuts import redirect, render
import hashlib
from hrmsApp.models import *

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Create your views here.
#Base
def base(request):
    return render(request, 'base.html')

#Super Admin Login
def superAdminLogin(request):
    return render(request, 'super_admin_login.html')

#Admin Login
def adminLogin(request):
    return render(request, 'admin_login.html')

#Employee Login
def employeeLogin(request):
    return render(request, 'employee_login.html')

#Admin Registration
def adminRegistration(request):
    return render(request, 'admin_registration.html')
#Employee Registration
from hrmsApp.models import Employee
def employeeRegistration(request): 
    if request.method=="POST":
        try:  
            employee_registrarion(request)
        except Exception as e:
            return HttpResponse(e)
    return render(request, 'employee_registration.html')


# TODO Rename this here and in `employeeRegistration`
def employee_registrarion(request):
            employee=Employee()
    employee.emp_id=Employee.objects.count()+1
    employee.name=request.POST.get('name')
    employee.username=request.POST.get('username')
    employee.designation=request.POST.get('designation')
    employee.contact=request.POST.get('contact')
    employee.alternative_contact=request.POST.get('alternative_contact')
    employee.blood_group=request.POST.get('blood_group')
    employee.personal_email=request.POST.get('personal_email')
    employee.company_email=request.POST.get('company_email')
    employee.date_of_birth=request.POST.get('date_of_birth')
    employee.current_address=request.POST.get('current_address')
    employee.permanent_address=request.POST.get('permanent_address')
    employee.password=hash_password(request.POST.get('password'))
    employee.save()