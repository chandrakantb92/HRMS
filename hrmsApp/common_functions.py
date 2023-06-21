import datetime
from django.shortcuts import redirect, render
from hrmsApp.models import*
from hrmsApp import template
from django.forms.models import model_to_dict
from hrmsProject import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

"""
Function to calculate number of work days, salary amount, deduction
"""
def calculatePaySlip(request,id):
    employee=Employee.objects.get(id=id)
    
    slip={
        'month':request.POST.get('month') ,
        'year': request.POST.get('year'),
        'emp_id': employee.id,
        'emp_name':employee.name ,
        'employee_designation':employee.designation,
        'paid_days': 24,
        'total_present_days': 24,
        'total_working_days': 31,
        'sankey_date_of_joining': EmployeeWorkDetails.objects.get(id=employee).date_of_joining ,
        'uan_number': EmployeeOfficialDetails.objects.get(id=employee).universal_acount_number ,
        'pesic':  EmployeeOfficialDetails.objects.get(id=employee).esic_number ,
        'account_no':EmployeeOfficialDetails.objects.get(id=employee).bank_acount_number ,
        'pancard':EmployeeOfficialDetails.objects.get(id=employee).pan ,
        'basic_salary':EmployeePackageDetails.objects.get(id=employee).basic_salary ,
        'hra_salary':EmployeePackageDetails.objects.get(id=employee).hra ,
        'traveling_allowance':EmployeePackageDetails.objects.get(id=employee).travell_allowance ,
        'medical_allowance':EmployeePackageDetails.objects.get(id=employee).medical_allowance  ,
        'other_allowance':EmployeePackageDetails.objects.get(id=employee).other_allowance  ,
        'arrears':0 ,
        'leave_encashment':0 ,
        'bonus':0 ,
        'provident_fund':Salary.objects.get(emp_id=employee).pf ,
        'mesic':0 ,
        'professional_tax':Salary.objects.get(emp_id=employee).professional_tax ,
        'other_charges':Salary.objects.get(emp_id=employee).other_charges ,
        'tds':Salary.objects.get(emp_id=employee).tds ,
        'advance':0,
        'gross_salary':EmployeePackageDetails.objects.get(id=employee).gross_salary  ,
        'total_deduction':(EmployeePackageDetails.objects.get(id=employee).gross_salary )-(EmployeePackageDetails.objects.get(id=employee).in_hand_salary ),
        'salary_in_hand':EmployeePackageDetails.objects.get(id=employee).in_hand_salary ,        
    }
    return render(request, 'slip.html',{'slip':slip})

def generateSlipData(slip):
    try:
        
        slip = model_to_dict(slip)
        employee=Employee.objects.get(id=int(slip['emp_id']))
        official = EmployeeOfficialDetails.objects.get(id=employee)
        work = EmployeeWorkDetails.objects.get(id=employee)
        package = EmployeePackageDetails.objects.get(id=employee)
        pesic =  EmployeeOfficialDetails.objects.get(id=employee).esic_number
        
        doj = work.date_of_joining
        email = employee.company_email
        uan_number = official.universal_acount_number
        account_no = official.bank_acount_number
        
        """Extracting and Replacing actual value into template"""
        slip_template = template.PAY_SLIP_TEMPLATE
        slip_template=slip_template.replace("month",slip['month'])
        slip_template=slip_template.replace("year",slip['year'])
        slip_template=slip_template.replace("emp_id", str(employee.id))
        slip_template=slip_template.replace("emp_name", str(employee.name))
        slip_template=slip_template.replace("emp_name", str(employee.name))
        slip_template=slip_template.replace("employee_designation", str(employee.designation))
        slip_template=slip_template.replace("paid_days", str(slip['paid_days']))
        slip_template=slip_template.replace("total_present_days", str(slip['total_present_days']))
        slip_template=slip_template.replace("total_working_days", str(slip['total_working_days']))
        slip_template=slip_template.replace("sankey_date_of_joining", str(work.date_of_joining))
        slip_template=slip_template.replace("uan_number", str(official.universal_acount_number))
        slip_template=slip_template.replace("pesic", str(official.esic_number))
        slip_template=slip_template.replace("account_no", str(official.bank_acount_number))
        slip_template=slip_template.replace("sankey_date_of_joining", str(work.date_of_joining))
        slip_template=slip_template.replace("pancard", str(official.pan))
        slip_template=slip_template.replace("basic_salary", str(slip['basic']))
        slip_template=slip_template.replace("hra_salary", str(slip['hra']))
        slip_template=slip_template.replace("traveling_allowance", str(slip['travel_allowence']))
        slip_template=slip_template.replace("medical_allowance", str(slip['medical_allowence']))
        slip_template=slip_template.replace("other_allowance", str(slip['other_allowence']))
        slip_template=slip_template.replace("arrears", str(slip['arrears']))
        slip_template=slip_template.replace("leave_encashment", str(slip['leave_encashment']))
        slip_template=slip_template.replace("bonus", str(slip['bonus']))
        slip_template=slip_template.replace("provident_fund", str(slip['provident_fund']))
        slip_template=slip_template.replace("mesic", str(slip['esic']))
        slip_template=slip_template.replace("professional_tax", str(slip['professional_tax']))
        slip_template=slip_template.replace("other_charges", str(slip['other_charges']))
        slip_template=slip_template.replace("tds", str(slip['tds']))
        slip_template=slip_template.replace("advance", str(slip['advances']))
        slip_template=slip_template.replace("gross_salary", str(package.gross_salary))
        slip_template=slip_template.replace("total_deduction", str(slip['total_deduction']))
        slip_template=slip_template.replace("salary_in_hand", str(slip['net_pay']))
        return ({'data': slip_template, 'email': email})
    except Exception as e:
        print(e)
       
def send_slip_email(email,template):
    try:
        text = template

        from_email = settings.DEFAULT_FROM_EMAIL
        to_email=[email]
        to_email=['Chandrakant.b@sankeysolutions.com']
        msg = EmailMultiAlternatives(
            "slip", text ,from_email, to_email)
        msg.attach_alternative(text,"text/html")
        msg.send()
        print("Mail sent successfully")
        return True
    except Exception as e:
        print(e)
        return False