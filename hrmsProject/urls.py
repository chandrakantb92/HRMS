"""
URL configuration for hrmsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from hrmsApp.views import *
from django.conf.urls import handler404
from django.conf import settings
#Urls pattern and their paths
urlpatterns = [
    
    path('',base, name='base'),
    path('admin/', admin.site.urls),
    path('base/', base, name='base'),
    path('superAdminLogin/', superAdminLogin, name='superAdminLogin'),
    path('adminLogin/', adminLogin, name='adminLogin'),
    path('employeeLogin/', employeeLogin, name='employeeLogin'),
    path('adminRegistration/', adminRegistration, name='adminRegistration'),
    path('employeeRegistration/', employeeRegistration, name='employeeRegistration'),
    path('employeeEducationRegistration/', employeeEducationRegistration, name='employeeEducationRegistration'),
    path('employeeWorkExperienceRegistration/', employeeWorkExperienceRegistration, name='employeeWorkExperienceRegistration'),
    path('employeeWorkDetailsRegistration/', employeeWorkDetailsRegistration, name='employeeWorkDetailsRegistration'),
    path('employeeOfficialDetails/', employeeOfficialDetails, name='employeeOfficialDetails'),
    path('employeePackageRegistration/', employeePackageRegistration, name='employeePackageRegistration'),
    path('salaryRegistration/', salaryRegistration, name='salaryRegistration'),
    path('employeeLeaveRegistration/', employeeLeaveRegistration, name='employeeLeaveRegistration'),
    path('holidayRegistration/', holidayRegistration, name='holidayRegistration'),
    path('employeeHome/', employeeHome, name='employeeHome'),
    path('employeeProfile/', employeeProfile, name='employeeProfile'),
    path('employeeHoliday/', employeeHoliday, name='employeeHoliday'),
    path('employeeLeave/', employeeLeave, name='employeeLeave'),
    path('resetEmployeePassword/', resetEmployeePassword, name='resetEmployeePassword'),
    path('resetAdminPassword/', resetAdminPassword, name='resetAdminPassword'),
    path('adminLogout/', adminLogout, name='adminLogout'),
    path('employeeLogout/', employeeLogout, name='employeeLogout'),
    path('header/', header, name='header'),
    path('adminHome/', adminHome, name='adminHome'),
    path('aproveLeave/', aproveLeave, name='aproveLeave'),
    path('viewAllLeave/', viewAllLeave, name='viewAllLeave'),
    path('viewAllEmployee/', viewAllEmployee, name='viewAllEmployee'),
    path('empAttendance/',  empAttendance, name='empAttendance'),
    path('attendanceSection/',  attendanceSection, name='attendanceSection'),
    path('employeePaySleep/',  employeePaySleep, name='employeePaySleep'),
    path('resetEmpPasswordByEmployee/',  resetEmpPasswordByEmployee, name='resetEmpPasswordByEmployee'),
    path('forgetPassword/',  forgetPassword, name='forgetPassword'),
    path('verifyOTP/',  verifyOTP, name='verifyOTP'),
    path('updateEmployeePersonal/', updateEmployeePersonal, name='updateEmployeePersonal'),
    path('updateEmployeeEducational/', updateEmployeeEducational, name='updateEmployeeEducational'),
    path('updateEmployeeOfficial/', updateEmployeeOfficial, name='updateEmployeeOfficial'),
    
    
    
    #path('<path:not_found>', handler404),
    
    re_path(r'^.*/$', page_not_available, name='page_not_available'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)