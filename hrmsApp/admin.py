from django.contrib import admin
from hrmsApp.models import *
# Register your models here.
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ( 'emp_id', 'name', 'username', 'designation' , 'contact' , 'alternative_contact' , 'blood_group' , 'aadhaar' , 'pan' , 'personal_email', 
#     'company_email' , 'role' , 'date_of_birth' , 'current_address' , 'permanent_address' , 'password')
    
# class EmpEduDetAdmin(admin.ModelAdmin):
#     list_display=('emp', 'ssc_school_name', 'ssc_passout_year', 'ssc_percentage', 'hsc_college_name', 'hsc_passout_year', 'hsc_stream', 'hsc_percentage',
#     'ug_college_name', 'ug_passout_year', 'ug_stream', 'ug_specialization', 'ug_percentage','pg_college_name','pg_passout_year', 'pg_stream',
#     'pg_specialization', 'pg_percentage', 'education_gap', 'gap_reason')
    

admin.site.register(Employee)
admin.site.register(EmployeeEducationDetails)