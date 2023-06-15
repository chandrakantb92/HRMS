from django.db import models

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=50)  
    description = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Technology"
    
#Employee table
class Employee(models.Model):
    emp_id = models.CharField(max_length=20, db_index=True, unique=True)
    name = models.CharField(max_length=100, db_index=True)
    username = models.EmailField(max_length=50, unique=True, db_index=True)
    designation = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    alternative_contact = models.CharField(max_length=15, blank=True)
    blood_group = models.CharField(max_length=5)
    aadhaar = models.CharField(max_length=15)
    pan = models.CharField(max_length=10)
    personal_email = models.CharField(max_length=50, blank=True)
    company_email = models.EmailField(max_length=50, blank=True)
    role = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    current_address = models.TextField()
    permanent_address = models.TextField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.emp_id
    
    class Meta:
        verbose_name = "employee"
        
from django.db import models

#Employee Education Detail
class EmployeeEducationDetails(models.Model):
    emp=models.ForeignKey(Employee, db_index=True, on_delete=models.CASCADE)
    ssc_school_name=models.CharField(max_length=50)
    ssc_passout_year=models.CharField(max_length=5)
    ssc_percentage=models.FloatField()
    hsc_college_name=models.CharField(max_length=50)
    hsc_passout_year=models.CharField(max_length=5)
    hsc_stream=models.CharField(max_length=5)
    hsc_percentage=models.FloatField()
    ug_college_name=models.CharField(max_length=50)
    ug_passout_year=models.CharField(max_length=5)
    ug_stream=models.CharField(max_length=5)
    ug_specialization=models.CharField(max_length=5)
    ug_percentage=models.FloatField()
    pg_college_name=models.CharField(max_length=50)
    pg_passout_year=models.CharField(max_length=5)
    pg_stream=models.CharField(max_length=5)
    pg_specialization=models.CharField(max_length=5)
    pg_percentage=models.FloatField()
    education_gap=models.CharField(max_length=10, blank=True, null=True)
    gap_reason=models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.addr
    class Meta:
        verbose_name = "employee_education_details"