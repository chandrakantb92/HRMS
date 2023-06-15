from django import forms
from datetime import datetime
from hrmsApp.models import *
from hrmsApp.views import userObj
# class MonthDataForm(forms.Form):
#     year_choices = [(year, year) for year in range(EmployeeWorkDetails.objects.get(id=userObj()).date_of_joining.year,  datetime.now().year+1)]
#     month_choices = [
#         (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
#         (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'),
#         (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')
#     ]

#     year = forms.ChoiceField(choices=year_choices, label='Year')
#     month = forms.ChoiceField(choices=month_choices, label='Month')