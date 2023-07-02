# import datetime
# from django.shortcuts import redirect, render
from hrmsApp.models import*
from hrmsApp import constants, template
#from django.forms.models import model_to_dict
from hrmsProject import settings
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
from django.utils.html import strip_tags
from xhtml2pdf import pisa
from io import BytesIO
from reportlab.lib import pdfencrypt
import pdfkit
import PyPDF2
# import json
from django.views.decorators.csrf import csrf_exempt
# from  datetime import datetime
# from datetime import timedelta
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models import Q
# from django.template import Context, Template
from io import BytesIO
import datetime,sys,os
from datetime import date
import calendar




"""
Function to calculate number of work days, salary amount, deduction
"""
def generateSlipData(slip_num):
    try:
        slip=EmployeePSlip.objects.get(slip_num=slip_num)
        employee = Employee.objects.get(id=slip.emp_id.id)
        official = EmployeeOfficialDetails.objects.get(id=employee)
        work = EmployeeWorkDetails.objects.get(id=employee)
        package = EmployeePackageDetails.objects.get(id=employee)
        slip_template = template.PAY_SLIP_TEMPLATE
        slip_template=slip_template.replace("month",slip.month)
        slip_template=slip_template.replace("year",slip.year)
        slip_template=slip_template.replace("emp_id", str(employee.id))
        slip_template=slip_template.replace("emp_name", str(employee.name))
        slip_template=slip_template.replace("emp_name", str(employee.name))
        slip_template=slip_template.replace("employee_designation", str(employee.designation))
        slip_template=slip_template.replace("paid_days", str(slip.paid_days))
        slip_template=slip_template.replace("total_present_days", str(slip.total_present_days))
        slip_template=slip_template.replace("total_working_days", str(slip.total_working_days))
        slip_template=slip_template.replace("sankey_date_of_joining", str(work.date_of_joining))
        slip_template=slip_template.replace("uan_number", str(official.universal_acount_number))
        slip_template=slip_template.replace("pesic", str(official.esic_number))
        slip_template=slip_template.replace("account_no", str(official.bank_acount_number))
        slip_template=slip_template.replace("sankey_date_of_joining", str(work.date_of_joining))
        slip_template=slip_template.replace("pancard", str(official.pan))
        slip_template=slip_template.replace("basic_salary", str(slip.basic))
        slip_template=slip_template.replace("hra_salary", str(slip.hra))
        slip_template=slip_template.replace("traveling_allowance", str(slip.travel_allowence))
        slip_template=slip_template.replace("medical_allowance", str(slip.medical_allowence))
        slip_template=slip_template.replace("other_allowance", str(slip.other_allowence))
        slip_template=slip_template.replace("arrears", str(slip.arrears))
        slip_template=slip_template.replace("leave_encashment", str(slip.leave_encashment))
        slip_template=slip_template.replace("bonus", str(slip.bonus))
        slip_template=slip_template.replace("provident_fund", str(slip.provident_fund))
        slip_template=slip_template.replace("mesic", str(slip.esic))
        slip_template=slip_template.replace("professional_tax", str(slip.professional_tax))
        slip_template=slip_template.replace("other_charges", str(slip.other_charges))
        slip_template=slip_template.replace("tds", str(slip.tds))
        slip_template=slip_template.replace("advance", str(slip.advances))
        slip_template=slip_template.replace("gross_salary", str(int(package.gross_salary)/12))
        slip_template=slip_template.replace("total_deduction", str(slip.total_deduction))
        slip_template=slip_template.replace("salary_in_hand", str(slip.net_pay))
        print("Template converted successfully")
        return slip_template
    except Exception as e:
        print(e)
        return False

def send_slip_email(pdf, credentials):
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [credentials['email']]
        subject = "Monthly Salary Slip"
        text_content = f"Please find attached your monthly salary slip of {credentials['month']} -  {credentials['year']}. Password is your Date of birth."
        msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        msg.attach(f"{credentials['name']}_{credentials['month']}-{credentials['year']}_Salary_slip.pdf", pdf,'application/pdf')
        msg.send()
        print("Mail sent successfully")
        return True
    except Exception as e:
        print(e)
        return False
    
def render_to_pdf(html_template: str, dob):
    try:
        dob=str(dob)
        password = ""
        password = ''.join(dob.split('-')[::-1])
        print("print 1")
        output_data = BytesIO()
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
       
        pdf_data = pdfkit.from_string(html_template , False, options={'quiet': ''}, configuration=config)
      
        pdf_reader = PyPDF2.PdfFileReader(BytesIO(pdf_data))
        pdf_writer = PyPDF2.PdfFileWriter()
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_writer.encrypt(password)
        pdf_writer.write(output_data)
        return output_data.getvalue()
    except Exception as error:
        print(error)
        return False


"""Getting employee month data"""
def get_employee_month_data(emp_id, month_name, year):  # sourcery skip: inline-immediately-returned-variable, remove-unnecessary-cast
    try:
        employee = Employee.objects.get(id = emp_id)
        month = constants.MONTH_DICTIONARY.get(month_name, None)
        total_day = (calendar.monthrange(year, month)[1] )
        start_date = date(year,month,1)
        end_date = date(year,month,total_day)
        if employee_attendence := get_employee_attendence(employee, start_date,end_date):
            if package_details:= get_employee_package_details(employee):
                if salary_details := get_employee_salary_details(employee):
                    leave_count = get_employee_leave_count(employee, month, year)
                    print("Employee attendence data retrived successfully")
                    employee_leave_taken_count = get_employee_leave_taken_count(employee, start_date,end_date)
                    holiday_count = get_holiday_count(year,month,total_day)
                    basic = int((float(package_details.basic_salary)) /12)
                    hra =  int((float(package_details.hra)) /12)
                    travell_allowance = int((float(package_details.travell_allowance)) /12)
                    medical_allowance = int((float(package_details.medical_allowance)) /12)
                    other_allowance = int((float(package_details.other_allowance)) /12)
                    esic = int((float(package_details.esic)) /12)
                    provident_fund = salary_details.pf
                    professional_tax = salary_details.professional_tax
                    other_charges = salary_details.other_charges
                    tds = salary_details.tds
                    total_deduction = int(provident_fund) - int(professional_tax) - int(other_charges) - int(tds)
                    total_earning = int(basic) + int(hra) + int(travell_allowance) + int(medical_allowance) + int(other_allowance) + int(esic)
                    # total_earning/=12
                    net_pay =int(total_earning) - (total_deduction)
                    data = {
                        'employee': employee,
                        'emp_id' : employee.id,
                        'month' : month_name,
                        'year' : year ,
                        'paid_days' : total_day,
                        'total_present_days' : float(employee_attendence),
                        'total_working_days' : float(employee_attendence) - float(holiday_count) - float(leave_count),
                        'basic' : basic,
                        'hra' : hra,
                        'travell_allowance' : travell_allowance,
                        'medical_allowance' : medical_allowance,
                        'other_allowance' : other_allowance,
                        'arrears' : 0,
                        'leave_encashment' : 0,
                        'bonus' : 0,
                        'provident_fund' :provident_fund,
                        'professional_tax' : professional_tax,
                        'other_charges' : 0,
                        'esic' : esic,
                        'tds' : tds,
                        'advances' : 0,
                        'total_deduction' : total_deduction,
                        'total_earning' : int(total_earning),
                        'net_pay' : net_pay,
                        'issued_date' : str( date.today() ),
                        'status' : False,
                        'created_by' : "",
                        'employee_leave_taken_count' : employee_leave_taken_count ,
                    }
                    return data
                return False
            return False
        return False
    except Exception as e:
        print(e)
        return False


"""Get employee attendence count from [perticular month"""
def get_employee_attendence(employee, start_date,end_date ):
    try:
        count = 0
        employee_attendence = EmployeeAttendance.objects.filter(Q(emp_id = employee) & Q(date__gte=start_date) & Q(date__lte=end_date) & Q(status=True))
        count += employee_attendence.count() if employee_attendence is not None else 0
        employee_attendence = EmployeeAttendance.objects.filter(Q(emp_id = employee) & Q(date__gte=start_date) & Q(date__lte=end_date) & Q(status=False))
        count2 = (employee_attendence.count() if employee_attendence is not None else 0) / 2
        return float( count+count2 )
    except Exception as e:
        return False
   
"""Get holiday count from holiday""" 
def get_holiday_count(year,month,day):
    try:
        start_date = date(year,month,1)
        end_date =  date(year,month,day)
        return Holiday.objects.filter(Q(date__gte=start_date) & Q(date__lte=end_date)).count()
    except Exception as e:
        print(e)
        return 0
    
"""Get employee leave count"""
def get_employee_leave_taken_count(employee, start_date,end_date):
    return 0   


"""Get Employee Salary Details per month"""
def get_employee_salary_details(employee):
    try:
        return Salary.objects.filter(emp_id=employee).first()
    except Exception as e:
        print(e)
        return False
    
"""Get Employee Package Details for One Annum"""
def get_employee_package_details(employee):
    try:
        return EmployeePackageDetails.objects.filter(id=employee).first()
    except Exception as e:
        print(e)
        return False
    
def get_employee_leave_count(employee,month, year):
    return 1