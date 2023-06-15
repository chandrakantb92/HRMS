from django.shortcuts import redirect, render
from hrmsApp.models import*

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