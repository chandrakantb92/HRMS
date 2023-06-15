from django.contrib import admin
from hrmsApp.models import *
#Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','name','username','designation','contact','alternative_contact','blood_group','personal_email','company_email','role','date_of_birth','current_address','permanent_address','image','password',)
    
class EmpEduDetAdmin(admin.ModelAdmin):
    list_display=('id','ssc_school_name','ssc_passout_year','ssc_percentage','hsc_college_name','hsc_passout_year','hsc_stream','hsc_percentage','ug_college_name','ug_passout_year','ug_stream','ug_specialization','ug_percentage','pg_college_name','pg_passout_year','pg_stream','pg_specialization','pg_percentage','education_gap','gap_reason')
    
class EmpWorkExpAdmin(admin.ModelAdmin):
    list_display=('id','company_name','designation','start_date','end_date','internship_company','internship_start_date', 'internship_end_date')
    
class EmpWorkDetAdmin(admin.ModelAdmin):
    list_display=('id', 'internship_start_date','internship_end_date','date_of_joining','date_of_leave')
    
class EmpOfficialDetAdmin(admin.ModelAdmin):
    list_display=('id','official_name','bank_name','bank_ifsc', 'bank_acount_number','aadhaar','pan','universal_acount_number','esic_number')
    
class EmpPackageAdmin(admin.ModelAdmin):
    list_display=('id','package','bonus','in_hand_salary','gross_salary','basic_salary','erf','hra','travell_allowance','medical_allowance','other_allowance','esic','pt')

class EmpLeaveAdmin(admin.ModelAdmin):
    list_display=('emp_id','leave_id','leave_type','leave_from','leave_till','number_of_days','leave_reason','is_aproved',  ) #'total_paid_leaves','used_paid_leaves','paid_leave_balance'

class LeaveAdmin(admin.ModelAdmin):
    list_display=('emp_id','total_paid_leaves','used_paid_leaves','paid_leave_balance','comp_off_leave')
    
class HolidayAdmin(admin.ModelAdmin):
    list_display=('id','name','date','day')
    
class EmpAttenAdmin(admin.ModelAdmin):
    list_display=('emp_id','date','in_time', 'out_time','status')
    
class SalaryAdmin(admin.ModelAdmin):
    list_display=('emp_id','pf','professional_tax','other_charges','tds')
    
class EmpLoginAdmin(admin.ModelAdmin):
    list_display=('emp_id','password','role','logindatetime')
    
class AdminsAdmin(admin.ModelAdmin):
    list_display=('emp_id','admin_username','password','role','date_of_registration')
    
class AdminLoginAdmin(admin.ModelAdmin):
    list_display=('admin_id','password','role','logindatetime')
    
#admin.site.register( , )    
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeEducationDetails, EmpEduDetAdmin)
admin.site.register(EmployeeWorkExperience, EmpWorkExpAdmin)
admin.site.register(EmployeeWorkDetails,EmpWorkDetAdmin)
admin.site.register(EmployeeOfficialDetails, EmpOfficialDetAdmin)
admin.site.register(EmployeePackageDetails, EmpPackageAdmin)
admin.site.register(EmployeeLeave, EmpLeaveAdmin)
admin.site.register(Leave,LeaveAdmin)
admin.site.register(Holiday, HolidayAdmin)
admin.site.register(EmployeeAttendance, EmpAttenAdmin)
admin.site.register(Salary, SalaryAdmin)
admin.site.register(EmployeeLogin, EmpLoginAdmin)
admin.site.register(Admins, AdminsAdmin)
admin.site.register(AdminLogin, AdminLoginAdmin)