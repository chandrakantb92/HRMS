from django.http import HttpResponse
from django.shortcuts import redirect, render
import hashlib
from hrmsApp.models import *
from django.db.models import Q
# Hash function
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

###########################################################################################
#Registration
# Employee registration
def employee_registrarion(request):
    try: 
        if isEmployeeExist(request):
            return HttpResponse("Something is duplicate")
        _extracted_from_employee_registrarion_4(request)
        return redirect('employeeEducationRegistration')
    except Exception as e:
        return HttpResponse(e)
    
#Admin Registration
def admin_registrarion(request):
    try:
        if isAdminExist(request):
            return HttpResponse("Something is duplicate")   
        _extracted_from_admin_registrarion_4(request)
        return redirect('base')
    except Exception as e:
        return HttpResponse(e)
    
    
# TODO Rename this here and in `employee_registrarion`
def _extracted_from_employee_registrarion_4(request):
    employee=Employee()
    employee.id=Employee.objects.count()+1
    employee.name=request.POST.get('name')
    employee.username=request.POST.get('username')
    employee.designation=request.POST.get('designation')
    employee.contact=request.POST.get('contact')
    employee.alternative_contact=request.POST.get('alternative_contact')
    employee.blood_group=request.POST.get('blood_group')
    employee.personal_email=request.POST.get('personal_email')
    employee.company_email=request.POST.get('company_email')
    employee.role=request.POST.get('role')
    employee.date_of_birth=request.POST.get('date_of_birth')
    employee.current_address=request.POST.get('current_address')
    employee.permanent_address=request.POST.get('permanent_address')
    employee.image=request.POST.get('image')
    employee.password=hash_password(request.POST.get('password'))
    employee.save() 
    
 # TODO Rename this here and in `admin_registrarion` 
def _extracted_from_admin_registrarion_4(request):
    admin=Admins(emp_id=(Employee.objects.get(id=(request.POST.get('emp_id')))))
    admin.admin_username=request.POST.get('admin_username')
    admin.password=hash_password(request.POST.get('confirm_password'))
    admin.role='admin'
    admin.save()
###########################################################################################

###########################################################################################
# Check is This employee Available??
def isEmployeeExist(request):
    try:
        return bool(Employee.objects.filter( Q(username=request.POST.get('username'))|
            Q(contact=request.POST.get('contact')) |
            Q(personal_email=request.POST.get('personal_email')) |
            Q(personal_email=request.POST.get('company_email'))
            ).exists())
    except Exception as e:
        return False

# Check is This employee Available??
def isAdminExist(request):
    try:
        return bool(Admins.objects.filter(admin_username=request.POST.get('admin_username')))
    except Exception as e:
        return False
    
###########################################################################################