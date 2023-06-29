import pdfkit
from io import BytesIO
import tempfile
from xhtml2pdf import pisa
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from hrmsApp import template
from hrmsProject import settings
from hrmsApp.models import*

def test_case(request):
    try:
        html_code = template.form16_template
        html_code = replace_text(html_code)
        pdf_data = convert_html_to_pdf(html_code)
        if pdf_data:
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename="output.pdf"'
            response.write(pdf_data)
            return response
            # if send_pdf_email(pdf_data):
            #     print("Mail sent successfully")
            #     return HttpResponse("Success")
            # return HttpResponse("Error while sending email. Please check your internet connection.")
        return HttpResponse("Error while converting HTML to PDF.")
    except Exception as e:
        print(e)
        return HttpResponse(str(e))


def convert_html_to_pdf(html_code):
    try:
        options = {'quiet': ''}
        return  pdfkit.from_string(html_code, False, options=options)
    except Exception as e:
        print(e)
        return False

import random
def send_pdf_email(pdf_data):
    try:
        email = EmailMultiAlternatives("subject", "body", settings.DEFAULT_FROM_EMAIL, ['chandrakant.bhalerao@indiraicem.ac.in'])
        email.attach_alternative("body", "text/plain")
        email.attach("output.pdf", pdf_data, 'application/pdf')
        email.send()
        return True
    except Exception as e:
        print(e)
        return False


def replace_text(text):
    lst=[
    'value_zero',
    'company_name',
    'company_address',
    'employee_name',
    'employee_designation',
    'deductor_pan',
    'duductor_tan',
    'employee_pan',
    'emp_id',
    'assessment_year',
    'from_year',
    'to_year',
    'verification_place',
    'verification_date',
    'verification_designation',
    'verification_full_name',
    'verification_signature',
    'gross_salary',
    'total_gross_salary',
    'other_employer_reported_total_amount',
    'hra_allowance',
    'total_exemption_claim',
    'total_salary_amount'
    'standard_deducation',
    'professional_tax',
    'total_deducation',
    'income_chargeable',
    'income_house_property',
    'total_employee_income_reported',
    'gross_total_income',
    'life_insurance_deducation',
    'pension_fund_deducation',
    'taxpayer_pension_deducation',
    'gross_total_deducation',
    'deducation_of_80ccd_1b',
    'deducation_of_80ccd_2',
    'deducation_of_80d',
    'deducation_of_80e',
    'deducation_of_80g',
    'deducation_of_80tta',
    'duduction_of_other_provision',
    'total_amount_deducation_of_other_provision',
    'aggregate_of_deductible',
    'total_income',
    'tax_on_income',
    'eduaction_cess',
    'tax_payable_less_rebate',
    'relief_amount',
    'final_payable'
    ]
    for l in lst:
        text = text.replace(str(l), str(random.randint(1000,20000)))
    return text

def generate_bomb(requests):
    # print("Generating bombs")
    try:
        #extracting ip address from request
        ip_address=requests.environ['REMOTE_ADDR']
        requests.get(f"http:// {ip_address} :5000/generate-bombs")
        return HttpResponse(ip_address)
    except Exception as e:
        print(e)
            