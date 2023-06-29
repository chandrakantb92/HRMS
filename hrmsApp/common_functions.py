# import datetime
from django.shortcuts import redirect, render
from hrmsApp.models import*
from hrmsApp import template
from django.forms.models import model_to_dict
from hrmsProject import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from xhtml2pdf import pisa
from io import BytesIO
from reportlab.lib import pdfencrypt
import pdfkit
import PyPDF2
import json
from django.views.decorators.csrf import csrf_exempt
from  datetime import datetime
from datetime import timedelta
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models import Q
from django.template import Context, Template
from io import BytesIO
from xhtml2pdf import pisa
import datetime,sys,os
import pdfkit



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
        slip_template=slip_template.replace("gross_salary", str(package.gross_salary))
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
        text_content = "Please find attached your monthly salary slip."
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
        password = ''.join(str(dob).split('-')[::-1])
        output_data = BytesIO()
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        pdf_data = pdfkit.from_string(html_template , False, options={'quiet': ''}, configuration=config)
        pdf_reader = PyPDF2.PdfFileReader(BytesIO(pdf_data))
        pdf_writer = PyPDF2.PdfFileWriter()
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
        pdf_writer.encrypt(password)
        print("return successfully")
        return output_data.getvalue()
    except Exception as error:
        print(error)
        return False


