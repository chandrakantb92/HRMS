#Libraries
import json
from pickle import EMPTY_DICT
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import hashlib
from hrmsApp.models import *
from datetime import date, datetime
from django.db.models import Sum
from hrmsApp.registration import*
from hrmsApp.common_functions import*
from hrmsProject import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from hrmsApp import template
from django.db.models import F
from django.contrib import admin

#Return id of loged in user(System Automation)
def logedUserId():
    return EmployeeLogin.objects.order_by('emp_id').first().emp_id.id

#Return id of loged in user(System Automation)
def logedAdminId():
    return (AdminLogin.objects.order_by('admin_id').first().admin_id.emp_id.id)
   
#return loged user object(System Automation)
def userObj():
    try:
        # lu = EmployeeLogin.objects.all().first()
        # return Employee.objects.get(id=lu.emp_id)
        # return EmployeeLogin.objects.first().emp_id.id
    
        return Employee.objects.get(id=logedUserId())
    except Exception as e:
        print(e)
        return None
     


#return is any employee has loged in or not(System Automation)
def isEmployeeLogedIn():
    return EmployeeLogin.objects.order_by('emp_id').first() is not None

#Check is Admin loged in or not(System Automation)
def isAdminLogedIn():
    return AdminLogin.objects.order_by('admin_id').first() is not None
  
#convert  password string to hash code(System Automation)
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Create your views here(For Everyone)
def base(request):
    return render(request, 'base.html')

#Super Admin Login(Super Admin)
def superAdminLogin(request):
    return render(request, 'super_admin_login.html')

#Admin Login(Admin)
def adminLogin(request):  # sourcery skip: extract-method
    if request.method=='POST':
        try:
            u=request.POST['username']
            p=hash_password(request.POST['password'])
            admin=Admins.objects.get(admin_username=u, password=p)
            if admin is not None:
                AdminLogin.objects.all().delete()
                login=AdminLogin()
                login.admin_id=admin
                login.password=p
                login.role='admin'
                login.save()
                return redirect('adminHome')
            return render(request, 'admin_login.html', {'error':'Invalid admin credentials'})
        except Exception as e:
            return render(request, 'admin_login.html', {'error':'Invalid admin credentials'})
    if isAdminLogedIn():
        return redirect('adminHome')
    return render(request, 'admin_login.html',{})

#Employee nLogin(Employee)
def employeeLogin(request):  # sourcery skip: extract-method
    if request.method=="POST":
        try:
            u=request.POST.get('username')
            p=hash_password(request.POST.get('password'))
            employee=Employee.objects.get(username=u, password=p)
            if employee is not None:
                EmployeeLogin.objects.all().delete()
                login=EmployeeLogin()
                login.emp_id=employee
                login.password=hash_password(hash_password(request.POST.get('password')))
                login.role='employee'
                login.save()
                return redirect('employeeHome')
            return render(request, 'employee_login.html', {'error':'Something went wrong'})
        except Exception as e:
            return render(request, 'employee_login.html', {'error':'Invalid username or password'})
    if isEmployeeLogedIn():
        return redirect('employeeHome')
    return render(request, 'employee_login.html')

#Employee Home(Employee)
def employeeHome(request):  # sourcery skip: avoid-builtin-shadow
    if isEmployeeLogedIn():
        balanceLeave(userObj())
        return render(request, 'employee_base.html',{'user':userObj(),'leave':Leave.objects.get(emp_id=userObj()),'empLeave':EmployeeLeave.objects.all().filter(emp_id=userObj()),'holidays': Holiday.objects.filter(date__gte=date.today()),'is_attendence':isAttendenceSaved,'in_attendance':isInAttendenceSaved,'out_attendance':isOutAttendenceSaved })
    return redirect('employeeLogin')

#Employee Profile page view (Employee) 
def employeeProfile(request):
    if isEmployeeLogedIn():
        return render(request, 'employee_profile.html',
                  {'user':userObj(), 
                    'empedudetails':EmployeeEducationDetails.objects.get(id=logedUserId()),
                    'empworkexpdetails':EmployeeWorkExperience.objects.get(id=logedUserId()),
                    'empworkdetails':EmployeeWorkDetails.objects.get(id=logedUserId()),
                    'empofficialdetail':EmployeeOfficialDetails.objects.get(id=logedUserId()),
                    'pcgdetail':EmployeePackageDetails.objects.get(id=logedUserId())
                    })
    return redirect('employeeLogin')

#View Holidays View(Employee)
def employeeHoliday(request):
    if isEmployeeLogedIn():
        return render(request, 'employee_holiday.html',
                {'user':userObj(),
                'holidays': Holiday.objects.all() 
                 } )
    return redirect('employeeLogin')

#View Employee Leave and Aply page(Employee)
def employeeLeave(request):
    if isEmployeeLogedIn():
        balanceLeave(userObj())
        return render(request, 'employee_leave.html',
                  {'user':userObj(),
                   'empLeave':EmployeeLeave.objects.all().filter(emp_id=logedUserId()),
                   } )
    return  redirect('employeeLogin')

#Admin Registration(Super Admin)
def adminRegistration(request):
    if request.method=="POST":
        try:
            emp_id=request.POST.get('emp_id')
            if emp_id is not None:
                return admin_registrarion(request)
            return render(request, 'admin_registration.html',{'error':'Limit Exceed' ,'employees':Employee.objects.exclude(id__in=Admins.objects.all().values_list('emp_id', flat=True))})
        except Exception as e:
            return HttpResponse(e)
    if isSuperAdminLogedIn():
        return render(request, 'admin_registration.html',{'employees':Employee.objects.exclude(id__in=Admins.objects.all().values_list('emp_id', flat=True))})
    return redirect('superAdminLogin')
  
#Super Admin Login(Super Admin):
def superAdminLogin(request):
    return HttpResponse("Super admin login required")
    # if request.method=="POST":
    #     try:
    #         s=1
    #     except Exception as e:
    #         print(e)
    # return redirect('base')

#Employee Registration view(Admin)
def employeeRegistration(request):   
    if request.method=="POST":
        try:
            return employee_registrarion(request)
        except Exception as e:
            return HttpResponse(e)
    if isSuperAdminLogedIn() :
        return render(request, 'employee_registration.html')
    return redirect('adminLogin')


#Employee Education Registration View(Admin)
def employeeEducationRegistration(request):
    if request.method=="POST":
        try:
            emp_id=request.POST.get('id')
            if emp_id is not None:
                employee = Employee.objects.get(id = emp_id) 
                education=EmployeeEducationDetails(id=employee,
                ssc_school_name=request.POST.get('ssc_school_name'),
                ssc_passout_year=request.POST.get('ssc_passout_year'),
                ssc_percentage=request.POST.get('ssc_percentage'),
                hsc_college_name=request.POST.get('hsc_college_name'),
                hsc_passout_year=request.POST.get('hsc_passout_year'),
                hsc_stream=request.POST.get('hsc_stream'),
                hsc_percentage=request.POST.get('hsc_percentage'),
                ug_college_name=request.POST.get('ug_college_name'),
                ug_passout_year=request.POST.get('ug_passout_year'),
                ug_stream=request.POST.get('ug_stream'),
                ug_specialization=request.POST.get('ug_specialization'),
                ug_percentage=request.POST.get('ug_percentage'),
                pg_college_name=request.POST.get('pg_college_name'),
                pg_passout_year=request.POST.get('pg_passout_year'),
                pg_stream=request.POST.get('pg_stream'),
                pg_specialization=request.POST.get('pg_specialization'),
                pg_percentage=request.POST.get('pg_percentage'),
                education_gap=request.POST.get('education_gap'),
                gap_reason=request.POST.get('gap_reason') )
                education.save()
                return redirect('employeeWorkExperienceRegistration')
            return render(request, 'employee_education_registration.html', {'error':'Invalid request'})
        except Exception as e:
            return HttpResponse(e)
    if isAdminLogedIn():
        return render(request, 'employee_education_registration.html', {'employees':Employee.objects.exclude(id__in=EmployeeEducationDetails.objects.all().values_list('id', flat=True))})
    return redirect('adminLogin')
    

#Employee Work Experience Registration view(Admin)
def employeeWorkExperienceRegistration(request):
    if request.method=="POST":
        try:
            employee=Employee.objects.get(id=request.POST.get('id'))
            work_experience=EmployeeWorkExperience(id=employee,
            company_name=request.POST.get('company_name'),
            designation=request.POST.get('designation'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
            internship_company=request.POST.get('internship_company'),
            internship_start_date=request.POST.get('internship_start_date'),
            internship_end_date=request.POST.get('internship_end_date') )
            work_experience.save()
            return redirect('employeeWorkDetailsRegistration')
        except Exception as e:
            return HttpResponse(e)
    if isAdminLogedIn():
        return render(request, 'employee_work_experience_registration.html', {'employees':Employee.objects.exclude(id__in=EmployeeWorkExperience.objects.all().values_list('id', flat=True))})
    return redirect('adminLogin')
    

#Employee Work Details Registration View(Admin)
def employeeWorkDetailsRegistration(request):  # sourcery skip: extract-method
    if request.method=="POST":
        try:
            employee=Employee.objects.get(id=request.POST.get('id'))
            work_details=EmployeeWorkDetails(id=employee,
            internship_start_date=request.POST.get('internship_start_date'),
            internship_end_date=request.POST.get('internship_end_date'),
            date_of_joining=request.POST.get('date_of_joining'),
            date_of_leave=request.POST.get('date_of_leave'))
            work_details.save()
            createLeave(employee)
            leaveAllowence()
            return redirect('employeeOfficialDetails')
        except Exception as e:
            return HttpResponse(e)
    if isAdminLogedIn():
        return render(request, 'employee_work_details_registration.html', {'employees':Employee.objects.exclude(id__in=EmployeeWorkDetails.objects.all().values_list('id', flat=True))})
    return redirect('adminLogin')
    
#Create View Function(System Automation)
def createLeave(employee):
    try:
        if leave:=Leave.objects.get(emp_id=employee):
            leave.save()
        leave=Leave.objects.create(emp_id=employee)
        leave.save()
    except Exception as e:
        print(e)
    
#Employee official details view(Admin)
def employeeOfficialDetails(request):
    if request.method=="POST":
        try:
            employee=Employee.objects.get(id=request.POST.get('id'))
            employee_official_details=EmployeeOfficialDetails(id=employee,
            official_name=request.POST.get('official_name'),
            bank_name=request.POST.get('bank_name'),
            bank_ifsc=request.POST.get('bank_ifsc'),
            bank_acount_number=request.POST.get('bank_acount_number'),
            aadhaar=request.POST.get('aadhaar'),
            pan=request.POST.get('pan'),
            universal_acount_number=request.POST.get('universal_acount_number'),
            esic_number=request.POST.get('esic_number'))
            employee_official_details.save()
            return redirect('employeePackageRegistration')
        except Exception as e:
            return HttpResponse(e)
    if isAdminLogedIn():
        return render(request, 'employee_official_details_registration.html', {'employees':Employee.objects.exclude(id__in=EmployeeOfficialDetails.objects.all().values_list('id', flat=True))})
    return redirect('adminLogin')
    

#Employee  Package Registration View(Admin)
def employeePackageRegistration(request):
    if request.method=="POST":
        try:
            employee=Employee.objects.get(id=request.POST.get('id'))
            employee_package=EmployeePackageDetails(id=employee,
            package=request.POST.get('package'),
            bonus=request.POST.get('bonus'),
            in_hand_salary=request.POST.get('in_hand_salary'),
            gross_salary=request.POST.get('gross_salary'),
            basic_salary=request.POST.get('basic_salary'),
            erf=request.POST.get('erf'),
            hra=request.POST.get('hra'),
            travell_allowance=request.POST.get('travell_allowance'),
            medical_allowance=request.POST.get('medical_allowance'),
            other_allowance=request.POST.get('other_allowance'),
            esic=request.POST.get('esic'),
            pt=request.POST.get('pt'))
            employee_package.save()
            return redirect('salaryRegistration')
            # return redirect('adminHome')
        except Exception as e:
            return HttpResponse(e)
    if isAdminLogedIn():
        return render(request, 'employee_package_registration.html', {'employees':Employee.objects.exclude(id__in=EmployeePackageDetails.objects.all().values_list('id', flat=True))})
    return redirect('adminLogin')
    
   
#Salary Registration View(Admin)
def salaryRegistration(request):
    if request.method=="POST":
        try:
            employee=Employee.objects.get(id=request.POST.get('id'))
            salary=Salary(emp_id=employee,
            pf=request.POST.get('pf'),
            professional_tax=request.POST.get('professional_tax'),
            other_charges=request.POST.get('other_charges'),
            tds=request.POST.get('tds')
            )
            salary.save()
            return redirect('adminHome')
        except Exception as e:
            return HttpResponse(e)
    if isAdminLogedIn():
        return render(request, 'salary_registration.html', {'employees':Employee.objects.exclude(id__in=Salary.objects.all().values_list('id', flat=True))})
    return redirect('adminLogin')
    



 #Holiday Registration(Admin)
def holidayRegistration(request):
    if request.method=="POST":
        try:
            holiday=Holiday.objects.create(name=request.POST.get('name'), date=request.POST.get('date'),day=request.POST.get('day') )
            return redirect('holidayRegistration')
        except Exception as e:
            return HttpResponse(e)
    if isAdminLogedIn():
        return render(request, 'holiday_registration.html', {'employees':Employee.objects.exclude(id__in=Holiday.objects.all().values_list('id', flat=True))})
    return redirect('adminLogin')  

#Employee Leave Registration(Employee)
def employeeLeaveRegistration(request):
    if request.method=="POST":
        try:
            employee=Employee.objects.get(id=logedUserId())
            leave=EmployeeLeave(emp_id=employee,
            leave_type=request.POST.get('leave_type'),
            leave_id=getLeaveCount()+1,
            leave_from=request.POST.get('leave_from'),
            leave_till=request.POST.get('leave_till'),
            number_of_days=request.POST.get('number_of_days'),
            leave_reason=request.POST.get('leave_reason'),
            is_aproved=False)
            leave.save()
            return redirect('employeeLeave')
        except Exception as e:
            return HttpResponse(e)
    if isEmployeeLogedIn():
        return render(request, 'employee_leave_registration.html', {'employees':Employee.objects.exclude(id__in=EmployeeLeave.objects.all().values_list('id', flat=True))})
    return redirect('employeeLogin')  
                    
#Generating unique leave Id(Automation)                             
def getLeaveCount():
    try:
        return EmployeeLeave.objects.order_by('-id').first().id
    except Exception as e:
        return 0
    
#Employee Password Reset View (Admin)
def resetEmployeePassword(request):
    if request.method=="POST":
        try:
                emp=Employee.objects.get(id=request.POST.get('id'))
                emp.password=hash_password(request.POST.get('cpassword'))
                emp.save()
                return redirect('resetEmployeePassword')
        except Exception as e:
            return HttpResponse(e)
    if isAdminLogedIn():
        return render(request, 'reset_employee_password.html', {'title':'Reset Employee Password', 'emp':Employee.objects.all()})
    return redirect('adminLogin')

#Admin Password Reset View
def resetAdminPassword(request):
    if request.method=="POST":
        try:
            admin=Admins.objects.get(emp_id=(Employee.objects.get(id=request.POST.get('id'))))
            admin.password=hash_password(request.POST.get('cpassword'))
            admin.save()
            return redirect('resetAdminPassword')
        except Exception as e:
            return HttpResponse(e)
    if isSuperAdminLogedIn():
        return render(request, 'reset_admin_password.html', {'title':'Reset Admin Password', 'admin':Admins.objects.all()})
    return redirect('superAdminLogin')
            
#Employee log out function(Employee/System Automation)
def employeeLogout(request):
    try:
        if isEmployeeLogedIn:
            EmployeeLogin.objects.all().delete()
            return redirect('base')
    except Exception as e:
        return HttpResponse(e)
 
 #Admin log out function(Admin/System Automation)
def adminLogout(request):
    try:
        if isAdminLogedIn:
            AdminLogin.objects.all().delete()
            return redirect('base')
    except Exception as e:
        return HttpResponse(e)   
    
#Header(system check) 
def header(request):
    return render(request, 'header.html')

#Admin Home page view(Admin)
def adminHome(request):
    if isAdminLogedIn():
        return render(request, 'admin_home.html')
    return redirect('adminLogin')

#Count month from two dates(System Automation)
def countMonth(date_of_joining):
    current_date=date.today()
    return ((current_date - date_of_joining).days )/30.4


# Employee Leave Allowence Automation functoin(Syatem Automation)
def leaveAllowence():
    try:
        leaves=Leave.objects.all()
        for leave in leaves:
            doj=EmployeeWorkDetails.objects.get(id=leave.emp_id).date_of_joining
            leave.total_paid_leaves=1+int(countMonth(doj))
            leave.paid_leave_balance=(leave.total_paid_leaves)-(leave.used_paid_leaves)-(leave.encashment_leave)
            leave.total_casual_leaves=1
            leave.save()
    except Exception as e:
        print(e)
   
#404_not_found custom page(System Automation) 
def page_not_available(request):
    return render(request, 'page_404.html')

#Employee aprove view(Admin)
def aproveLeave(request):
    if request.method=="POST" and request.POST.get('approve')=="Approved":
        try:
            l=EmployeeLeave.objects.get(leave_id=(request.POST.get('l_id')))
            l.is_aproved=True
            l.save()
            updateLeave(request.POST.get('e_id'))
            return redirect('aproveLeave')
        except Exception as e:
            return HttpResponse("Something went wrong thats why error occured!")
    return render(request, 'aprove_leave.html', {'employee_leaves': EmployeeLeave.objects.all().filter(is_aproved=False)})


#Update Leave Data(Call by Admin for System Automation)
def updateLeave(empId):
    try:
        employee=Employee.objects.get(id=empId)
        leave=Leave.objects.get(emp_id=employee)
        eleaves=EmployeeLeave.objects.filter(emp_id=employee,type='paid', is_aproved=True)
        cnt = sum(o.number_of_days for o in eleaves)
        leave.used_paid_leaves=cnt
        eleaves=EmployeeLeave.objects.filter(emp_id=employee,type='casual', is_aproved=True)
        cnt = sum(o.number_of_days for o in eleaves)
        leave.total_casual_leaves=cnt
        leave.paid_leave_balance=leave.total_paid_leaves-cnt
        leave.save()
        leaveAllowence()
        balanceLeave(employee)
    except Exception as e:
        print(e)
        
        
"""balave leave count"""
def balanceLeave(employee):
    try:
        leave = Leave.objects.get(emp_id = employee)
        totalleave = leave.total_paid_leaves
        empleaves = EmployeeLeave.objects.filter(emp_id=employee, leave_type ='paid', is_aproved = True)
        cnt = sum(o.number_of_days for o in empleaves)
        balance =totalleave- cnt-leave.encashment_leave
        leave.paid_leave_balance = balance
        leave.save() 
        empleaves = EmployeeLeave.objects.filter(emp_id=employee, leave_type ='casual', is_aproved = True)
        cnt = sum(o.number_of_days for o in empleaves)
        leave.total_casual_leaves = cnt
        leave.save()
        
    except Exception as e:
        print(e)
    
#View All Employee Leave(Admin)
def viewAllLeave(request):
    try:
        if isAdminLogedIn():
            leaves= EmployeeLeave.objects.all()
            return render(request, 'view_leave.html', {'employee_leaves':leaves})
        return redirect('adminLogin')
    except Exception as e:
        return HttpResponse('error')

#View All Employees(Admin)
def viewAllEmployee(request):
    try:
        if isAdminLogedIn():
            employees = Employee.objects.all().order_by('id')
            return render(request, 'view_employee.html', {'employees':employees})
        return redirect('adminLogin')
    except Exception as e:
        return HttpResponse('error')
    
#Is Super Admin Loged In?
def isSuperAdminLogedIn():
    return True

#Employee in attendance
def empInAttendance(request):
    if request.method=="POST":
        try:
            employee=Employee.objects.get(id=logedUserId())
            attendance=EmployeeAttendance(emp_id=employee)
            attendance.date=date.today()
            attendance.in_time=datetime.now().time()
            attendance.save()
            return redirect('employeeHome')
        except Exception as e:
            return HttpResponse(e)
    

#Employee out attendence
def empOutAttendance(request):
    if request.method=="POST":
        try:
            employee=Employee.objects.get(id=logedUserId())
            attendence=EmployeeAttendance.objects.get(emp_id=employee, date=date.today())
            attendence.out_time= datetime.now().time()
            attendence.status=True
            attendence.save()
            return redirect('employeeHome')
        except Exception as e:
            return HttpResponse(e)
    
#Employee Attendance
def empAttendance(request):
    if request.method=="POST":
        try:
            employee=Employee.objects.get(id=logedUserId())
            if isAttendenceSaved() is False:
                attendance=EmployeeAttendance(emp_id=employee)
                attendance.date=date.today()
                attendance.in_time=datetime.now().time()
                attendance.save()
                return redirect('employeeHome')
            attendance=EmployeeAttendance.objects.get(emp_id=employee, date=date.today())   
            if attendance.status is False:
                attendance.out_time=datetime.now().time()
                attendance.status=True
                attendance.save()
                return redirect('employeeHome')
        except Exception as e:
            return HttpResponse(e)
    return HttpResponse("Bad Request!")

#Employee Attendance Section View
def attendanceSection(request):
    try:
        if isEmployeeLogedIn():
            return render(request, 'employee_attendence_section.html', {'user':userObj() , 'attendances':EmployeeAttendance.objects.filter(emp_id=userObj())})
        return HttpResponse("Unauthorized Access")
    except Exception as e:
        return HttpResponse(e)

#Employee Pay slip view
def employeePaySleep(request):
    if request.method=="POST":
        try:
            return calculatePaySlip(request, logedUserId())
        except Exception as e:
            return HttpResponse(e)
    if isEmployeeLogedIn():
        years={2023}
        months={'January':1, 'February':2,'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11,'December':12}
        return render(request, 'employee_pay_slip.html', {'user':userObj() ,'years':years, 'months':months,'error':""})
    return HttpResponse("Bad Request!")

    

#Check is logedin employee todays attendance record is present or not
def isAttendenceSaved():
    try:
        employee=Employee.objects.get(id=logedUserId())
        return bool(
            EmployeeAttendance.objects.get(
                emp_id=employee, date=date.today()
            )
        )
    except Exception as e:
        return False
 
#Return true if loged user have saved their in attendence
def isInAttendenceSaved():
    try:
        employee=Employee.objects.get(id=logedUserId())
        return bool(
            EmployeeAttendance.objects.get(
                emp_id=employee, date=date.today(), status=False
            )
        )
    except Exception as e:
        return False  
 
 #Return true if loged user have saved their out attendence
def isOutAttendenceSaved():
    try:
        employee=Employee.objects.get(id=logedUserId())
        return bool(
            EmployeeAttendance.objects.get(
                emp_id=employee, date=date.today(), status=True
            )
        )
    except Exception as e:
        return False   

"""System generated email """
def sendMailOtp(otp,reicever_email):
    try:
        text = template.OTP_AUTHENTICATOIN_MAIL_TEMPLATE
        text=text.replace('mail_otp', str(otp))
        subject = 'Test email'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email=[reicever_email]
        to_email=['Chandrakant.b@sankeysolutions.com']
        msg = EmailMultiAlternatives(
            subject, text ,from_email, to_email)
        msg.attach_alternative(text,"text/html")
        msg.send()
        print("Mail sent successfully")
        time=str(datetime.now())
        return True
    except Exception as e:
        print(e)
        return False
 
"""Get employee by their username """
def getEmployeeByIdOrUsername(username):
    try:
        username = username
        return Employee.objects.get(username=username).id
    except Exception as e:
        return False

"""When employee forget password"""  
def forgetPassword(request):
    if request.method=="POST": 
        try:
            if emp_id := getEmployeeByIdOrUsername(request.POST.get('username')):
                otp = random.randint(100000,999999)
                employee = Employee.objects.get(id=emp_id)
                email = employee.company_email
                if sendMailOtp(otp,email):
                    OtpAuthentication.objects.all().delete()
                    auth = OtpAuthentication.objects.create(emp_id=employee, otp=str(otp))
                    return redirect('verifyOTP')
                return HttpResponse("Internal server error")
            return render(request, 'employee_send_otp.html',{'error':'User not found'})
        except Exception as e:
            return HttpResponse(e)
    return render(request, 'employee_send_otp.html',{'error':''})
    
"""Verify OTP (Employee->System)"""  
def verifyOTP(request):
    if request.method=="POST":
        try:
            sent_otp = OtpAuthentication.objects.first().otp
            entered_otp = int(( request.POST.get('digit1') + request.POST.get('digit2') + request.POST.get('digit3') +  request.POST.get('digit4') + request.POST.get('digit5') + request.POST.get('digit6') ))
            if str(sent_otp)==str(entered_otp):
                s = OtpAuthentication.objects.all().first()
                s.status = True
                s.save()
                return redirect("resetEmpPasswordByEmployee")
            return render(request, 'otp_verification.html',{'error':"OTP does not match"})
        except Exception as e:
            return HttpResponse(e)
    return render(request, 'otp_verification.html')

"""Reset employee Password (Employee)"""
def resetEmpPasswordByEmployee(request):
    try:
        if auth:= OtpAuthentication.objects.all().first():
            try:
                if request.method=="POST":
                    if auth.status==True:
                        employee = Employee.objects.get(id=auth.emp_id.id)
                        employee.password=hash_password(request.POST.get('password'))
                        employee.save()
                        OtpAuthentication.objects.all().delete()
                        return redirect('employeeLogin')
                    return redirect('forgetPassword')
                return render(request, 'reset_emp_password_by_employee.html')
            except Exception as e:
                print(e)
                return HttpResponse("Internal Server Error")  
        return JsonResponse({'status':401,'Message':'Unauthorised access'})     
    except Exception as e:
        print(e)
        return HttpResponse("Internal Server Error")  


Comment = """ Update Employee Information """

# Update Employee basic informattion
def updateEmployeePersonal(request):  # sourcery skip: extract-method
    if request.method=="POST":
        try:
            employee = Employee.objects.get(id=request.POST.get('emp_id'))
            employee.name = request.POST.get('name') if employee.name!=request.POST.get('name') else employee.name
            employee.contact = request.POST.get('contact') if employee.contact!=request.POST.get('contact') else employee.contact
            employee.alternative_contact = request.POST.get('alternative_contact') if employee.alternative_contact!=request.POST.get('alternative_contact') else employee.alternative_contact
            employee.blood_group = request.POST.get('blood_group') if employee.blood_group!=request.POST.get('blood_group') else employee.blood_group
            employee.personal_email = request.POST.get('personal_email') if employee.personal_email!=request.POST.get('personal_email') else employee.personal_email
            employee.date_of_birth = request.POST.get('date_of_birth') if employee.date_of_birth!=request.POST.get('date_of_birth') else employee.date_of_birth
            employee.current_address = request.POST.get('current_address') if employee.current_address!=request.POST.get('current_address') else employee.current_address
            employee.permanent_address = request.POST.get('permanent_address') if employee.permanent_address!=request.POST.get('permanent_address') else employee.permanent_address
            employee.password = hash_password(request.POST.get('password')) if employee.password!=hash_password(request.POST.get('password')) else employee.password
            employee.save()
            if isEmployeeLogedIn():
                return redirect('employeeProfile')
            if isAdminLogedIn():
                return redirect('viewAllEmployee')
            return HttpResponse("Who the hell are you")
        except Exception as e:
          print(e)
    emp_id=int(request.GET.get('emp_id'))
    if isEmployeeLogedIn():
        if emp_id != logedUserId():
            return JsonResponse({'status':401, 'message':'unauthorized access'})
        return render(request, 'update_employee_personal.html',{'employee':Employee.objects.get(id= emp_id)})   
    if isAdminLogedIn():
        return render(request, 'update_employee_personal.html',{'employee':Employee.objects.get(id= emp_id)})
    return redirect('employeeLogin')   

# Update employee Educational Details
def updateEmployeeEducational(request):  # sourcery skip: extract-method, low-code-quality
    if request.method=="POST":
        try:
            emp_id=request.POST.get('emp_id')
            if emp_id is not None:
                employee = Employee.objects.get(id=emp_id)
                educational = EmployeeEducationDetails.objects.get(id=employee)
                educational.ssc_school_name = request.POST.get('ssc_school_name') if educational.ssc_school_name!=request.POST.get('ssc_school_name') else educational.ssc_school_name
                educational.ssc_passout_year = request.POST.get('ssc_passout_year') if educational.ssc_percentage!=request.POST.get('ssc_passout_year') else educational.ssc_passout_year
                educational.ssc_percentage = request.POST.get('ssc_percentage') if educational.ssc_percentage!=request.POST.get('ssc_percentage') else educational.ssc_percentage
                educational.hsc_college_name = request.POST.get('hsc_college_name') if educational.hsc_college_name!=request.POST.get('hsc_college_name') else educational.hsc_college_name
                educational.hsc_passout_year = request.POST.get('hsc_passout_year') if educational.hsc_passout_year !=request.POST.get('hsc_passout_year') else educational.hsc_passout_year
                educational.hsc_stream = request.POST.get('hsc_stream') if educational.hsc_stream!=request.POST.get('hsc_stream') else educational.hsc_stream
                educational.hsc_percentage = request.POST.get('hsc_percentage') if educational.hsc_percentage!=request.POST.get('hsc_percentage') else educational.hsc_percentage
                educational.ug_college_name = request.POST.get('ug_college_name') if educational.ug_college_name!=request.POST.get('ug_college_name') else educational.ug_college_name
                educational.ug_passout_year = request.POST.get('ug_passout_year') if educational.ug_passout_year!=request.POST.get('ug_passout_year') else educational.ug_passout_year
                educational.ug_stream = request.POST.get('ug_stream') if educational.ug_stream!=request.POST.get('ug_stream') else educational.ug_stream
                educational.ug_specialization = request.POST.get('ug_specialization') if educational.ug_specialization!=request.POST.get('ug_specialization') else educational.ug_specialization
                educational.ug_percentage = request.POST.get('ug_percentage') if educational.hsc_stream!=request.POST.get('ug_percentage') else educational.ug_percentage
                educational.pg_college_name = request.POST.get('pg_college_name') if educational.pg_college_name!=request.POST.get('pg_college_name') else educational.pg_college_name
                educational.pg_passout_year = request.POST.get('pg_passout_year') if educational.pg_passout_year!=request.POST.get('pg_passout_year') else educational.pg_passout_year
                educational.pg_stream = request.POST.get('pg_stream') if educational.pg_stream!=request.POST.get('pg_stream') else educational.pg_stream
                educational.pg_specialization = request.POST.get('pg_specialization') if educational.pg_specialization!=request.POST.get('pg_specialization') else educational.pg_specialization
                educational.pg_percentage = request.POST.get('pg_percentage') if educational.pg_percentage!=request.POST.get('pg_percentage') else educational.pg_percentage
                educational.education_gap = request.POST.get('education_gap') if educational.education_gap!=request.POST.get('education_gap') else educational.education_gap
                educational.gap_reason = request.POST.get('gap_reason') if educational.gap_reason!=request.POST.get('gap_reason') else educational.gap_reason
                educational.save()
                if isEmployeeLogedIn():
                    return redirect('employeeProfile')
                if isAdminLogedIn():
                    return redirect('viewAllEmployee')
                return HttpResponse("Who are you")
            return JsonResponse({'status':400, 'message':'Invalid request body'})
        except Exception as e:
          print(e)
    emp_id=int(request.GET.get('emp_id'))
    if isEmployeeLogedIn():
        if emp_id != logedUserId():
            return JsonResponse({'status':401, 'message':'unauthorized access'})
        return render(request, 'update_employee_educational.html',{'educational':EmployeeEducationDetails.objects.get(id=(Employee.objects.get(id= emp_id)))})   
    if isAdminLogedIn():
        return render(request, 'update_employee_educational.html',{'educational':EmployeeEducationDetails.objects.get(id=(Employee.objects.get(id= emp_id)))})
    return redirect('employeeLogin')   


#Update Employee Official Details
def updateEmployeeOfficial(request): # sourcery skip: extract-method, last-if-guard
    if request.method=="POST":
        try:
            emp_id=request.POST.get('emp_id')
            print(emp_id)
            if emp_id is not None:
                employee = Employee.objects.get(id=emp_id)
                official = EmployeeOfficialDetails.objects.get(id=employee)
                official.official_name = request.POST.get('official_name') if official.official_name!=request.POST.get('official_name') else official.official_name
                official.bank_name = request.POST.get('bank_name') if official.bank_name!=request.POST.get('bank_name') else official.bank_name
                official.bank_ifsc = request.POST.get('bank_ifsc') if official.bank_ifsc!=request.POST.get('bank_ifsc') else official.bank_ifsc
                official.bank_acount_number = request.POST.get('bank_acount_number') if official.bank_acount_number!=request.POST.get('bank_acount_number') else official.official_name
                official.aadhaar = request.POST.get('aadhaar') if official.aadhaar!=request.POST.get('aadhaar') else official.aadhaar
                official.pan = request.POST.get('pan') if official.pan!=request.POST.get('pan') else official.pan
                official.universal_acount_number = request.POST.get('universal_acount_number') if official.universal_acount_number!=request.POST.get('universal_acount_number') else official.universal_acount_number
                official.esic_number = request.POST.get('esic_number') if official.esic_number!=request.POST.get('esic_number') else official.esic_number
                official.save()
                if isEmployeeLogedIn():
                    return redirect('employeeProfile')
                if isAdminLogedIn():
                    return redirect('viewAllEmployee')
                return HttpResponse("Who are you")
            return JsonResponse({'status':400, 'message':'Invalid request body'})
        except Exception as e:
          print(e)
          return JsonResponse({'status':500, 'message':'Internal server error'})
    emp_id=int(request.GET.get('emp_id'))
    if isAdminLogedIn():
        return render(request, 'update_employee_official.html',{'official':EmployeeOfficialDetails.objects.get(id=(Employee.objects.get(id= emp_id))), 'isAdminLogedIn':True})
    if isEmployeeLogedIn():
        if emp_id != logedUserId():
            return JsonResponse({'status':401, 'message':'unauthorized access'})
        return render(request, 'update_employee_official.html',{'official':EmployeeOfficialDetails.objects.get(id=(Employee.objects.get(id= emp_id))), 'isEmployeeLogedIn':True})   
    return redirect('employeeLogin') 

#Update Employee Package Details
def updateEmployeePackage(request):
    if request.method=="POST":
        try:
            emp_id=request.POST.get('emp_id')
            print(emp_id)
            if emp_id is not None:
                employee = Employee.objects.get(id=emp_id)
                # official = EmployeeOfficialDetails.objects.get(id=employee)
                # official.save()
                return redirect('viewAllEmployee')
            return JsonResponse({'status':400, 'message':'Invalid request body'})
        except Exception as e:
          print(e)
          return JsonResponse({'status':500, 'message':'Internal server error'})
    emp_id=int(request.GET.get('emp_id'))
    if isAdminLogedIn():
        return render(request, 'update_employee_package.html',{'official':EmployeeOfficialDetails.objects.get(id=(Employee.objects.get(id= emp_id))), 'isAdminLogedIn':True})
    return redirect('adminLogin') 
