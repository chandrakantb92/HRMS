from django.db import models

    
#Employee table
class Employee(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    username = models.EmailField(max_length=50, unique=True, db_index=True)
    designation = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    alternative_contact = models.CharField(max_length=15, blank=True)
    blood_group = models.CharField(max_length=5)
    gender = models.CharField(max_length=10, default="")
    personal_email = models.CharField(max_length=50, blank=True)
    company_email = models.EmailField(max_length=50, blank=True)
    role = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    current_address = models.TextField()
    permanent_address = models.TextField()
    image=models.ImageField(null=True, blank=True, upload_to='images/')
    password=models.CharField(max_length=100)
    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = "employees"

#Employee Education Detail
class EmployeeEducationDetails(models.Model):
    id=models.OneToOneField(Employee, primary_key=True, on_delete=models.CASCADE)
    ssc_school_name=models.CharField(max_length=50)
    ssc_passout_year=models.CharField(max_length=5 , null=True)
    ssc_percentage=models.FloatField()
    hsc_college_name=models.CharField(max_length=50)
    hsc_passout_year=models.CharField(max_length=5)
    hsc_stream=models.CharField(max_length=50)
    hsc_percentage=models.FloatField()
    ug_college_name=models.CharField(max_length=50)
    ug_passout_year=models.CharField(max_length=5)
    ug_stream=models.CharField(max_length=50)
    ug_specialization=models.CharField(max_length=50)
    ug_percentage=models.FloatField()
    pg_college_name=models.CharField(max_length=50)
    pg_passout_year=models.CharField(max_length=5)
    pg_stream=models.CharField(max_length=50)
    pg_specialization=models.CharField(max_length=50)
    pg_percentage=models.FloatField()
    education_gap=models.CharField(max_length=10, blank=True, null=True)
    gap_reason=models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = "employees_education_details"
    
# Employee Work Experience model        
class EmployeeWorkExperience(models.Model):
    id=models.OneToOneField(Employee, primary_key=True, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    start_date=models.DateField()
    end_date=models.DateField()
    internship_company=models.CharField(max_length=50)
    internship_start_date=models.DateField()
    internship_end_date=models.DateField()
    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = "employees_work_experience"
        
#Employe Work details
class EmployeeWorkDetails(models.Model):
    id=models.OneToOneField(Employee, primary_key=True, on_delete=models.CASCADE)
    internship_start_date=models.DateField()
    internship_end_date=models.DateField()
    date_of_joining=models.DateField()
    date_of_leave=models.DateField()
    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = "employees_work_details"
    
# Employee Official Details model
class EmployeeOfficialDetails(models.Model):
    id=models.OneToOneField(Employee, primary_key=True, on_delete=models.CASCADE)
    official_name=models.CharField(max_length=50)
    bank_name=models.CharField(max_length=50)
    bank_ifsc=models.CharField(max_length=20)
    bank_acount_number=models.CharField(max_length=30)
    aadhaar=models.CharField(max_length=15)
    pan=models.CharField(max_length=10)
    universal_acount_number=models.CharField(max_length=50)
    esic_number=models.CharField(max_length=15)
    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = "employees_official_details"
        
#Employee Package Details 
class EmployeePackageDetails(models.Model):
    id=models.OneToOneField(Employee, primary_key=True, on_delete=models.CASCADE)
    package=models.FloatField()
    bonus=models.FloatField()
    in_hand_salary=models.FloatField()
    gross_salary=models.FloatField()
    basic_salary=models.FloatField()
    erf=models.FloatField()
    hra=models.FloatField()
    travell_allowance=models.FloatField()
    medical_allowance=models.FloatField()
    other_allowance=models.FloatField()
    esic=models.FloatField()
    pt=models.FloatField()
    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = "employees_package_details"
        
#Employee leave model
class EmployeeLeave(models.Model):
    emp_id=models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_id=models.IntegerField()
    leave_type=models.CharField(max_length=30)
    leave_from=models.DateField()
    leave_till=models.DateField()
    number_of_days=models.IntegerField()
    leave_reason=models.TextField()
    is_aproved=models.BooleanField(default=False)
    def _str__(self):
        return str(self.emp_id)
    class Meta:
        db_table = "employees_leave"
        
class Leave(models.Model):
    emp_id=models.ForeignKey(Employee, on_delete=models.CASCADE)
    total_paid_leaves=models.IntegerField(default=1)
    used_paid_leaves=models.IntegerField(default=0)
    paid_leave_balance=models.IntegerField(default=1)
    comp_off_leave=models.IntegerField(default=0)
    encashment_leave = models.IntegerField(default=0)
    total_casual_leaves=models.IntegerField(default=0)
    def __str__(self):
        return str(self.emp_id)
    class Meta:
        db_table = "leave"
list_display=('emp_id','total_paid_leaves','used_paid_leaves','paid_leave_balance','comp_off_leave','encashment_leave','total_casual_leaves')
        
#Holiday Model
class Holiday(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    date=models.DateField()
    day=models.CharField(max_length=20)
    def __str__(self):
        return str(self.name)
    class Meta:
        db_table = "holidays"
      

#Employee Attendence Model
class EmployeeAttendance(models.Model):
    emp_id=models.ForeignKey(Employee, on_delete=models.CASCADE)
    date=models.DateField()
    in_time=models.TimeField(blank=True, null=True)
    out_time=models.TimeField(blank=True, null=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.emp_id)
    class Meta:
        db_table = "employees_attendance"

#Salary Model
class Salary(models.Model):
    emp_id=models.ForeignKey(Employee, on_delete=models.CASCADE)
    pf=models.FloatField()
    professional_tax=models.FloatField()
    other_charges=models.FloatField()
    tds=models.FloatField()
    def __str__(self):
        return str(self.emp_id)
    class Meta:
        db_table = "salary"

#Employee login session model
class EmployeeLogin(models.Model):
    emp_id=models.ForeignKey(Employee, on_delete=models.CASCADE)
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=20, blank=False)
    logindatetime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.emp_id)
    class Meta:
        db_table = "employee_login"
        
#Admin Model
class Admins(models.Model):
    emp_id=models.ForeignKey(Employee, on_delete=models.CASCADE)
    admin_username=models.CharField(max_length=20)
    password=password=models.CharField(max_length=100)
    role=models.CharField(max_length=20, blank=False)
    date_of_registration=models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.emp_id)
    class Meta:
        db_table = "admins"
        
#Admin Login Model
class AdminLogin(models.Model):
    admin_id=models.ForeignKey(Admins, on_delete=models.CASCADE)    
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=20, blank=False)
    logindatetime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.admin_id.emp_id.name
    class Meta:
        db_table = "admin_login"
   
#Employee otp verification     
class OtpAuthentication(models.Model):
    emp_id=models.ForeignKey(Employee, on_delete=models.CASCADE)
    time=models.TimeField(auto_now=True)
    otp=models.CharField(max_length=6,blank=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.emp_id.name)
    class Meta:
        db_table="otpauthentication"
  
#Employee pay slip model      
class EmployeePSlip(models.Model):
    slip_num = models.IntegerField(default=0)
    emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    month=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    paid_days=models.CharField(max_length=20, default='0') 
    total_present_days=models.CharField(max_length=20, default='0')
    total_working_days=models.CharField(max_length=20, default='0')    
    basic=models.CharField(max_length=20, default='0')
    hra=models.CharField(max_length=20,default='0')
    travel_allowence=models.CharField(max_length=20,default='0')
    medical_allowence=models.CharField(max_length=20,default='0')
    other_allowence=models.CharField(max_length=20,default='0')
    arrears=models.CharField(max_length=20,default='0')
    leave_encashment=models.CharField(max_length=20,default='0')
    bonus=models.CharField(max_length=20,default='0')
    provident_fund=models.CharField(max_length=20,default='0')
    esic=models.CharField(max_length=20,default='0')
    professional_tax=models.CharField(max_length=20,default='0')
    other_charges=models.CharField(max_length=20,default='0')
    tds=models.CharField(max_length=20,default='0')
    advances=models.CharField(max_length=20,default='0')
    total_deduction=models.CharField(max_length=20,default='0')
    total_earning=models.CharField(max_length=20,default='0')
    net_pay=models.CharField(max_length=20,default='0')
    issued_date=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    created_by=models.CharField(max_length=50)
    def __str__(self):
        return str(self.emp_id.name)
    class Meta:
        db_table="employee_pay_slip"

