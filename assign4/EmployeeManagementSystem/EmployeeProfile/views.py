from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Employee, Department

def employee_list(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def department_list(request):
    department_details_data = [
        {'id': 0, 'd_name': 'Computer Science', 'location': 'right corner', 'job drscritopn': 'Head of department'},
        {'id': 1, 'd_name': 'English', 'location': 'first corner', 'job description': 'head'},
        {'id': 2, 'd_name': 'CHEMOSTRY', 'location': 'left corner', 'job description': 'head'},
        {'id': 3, 'd_name': 'Managemaent scinec', 'location': 'last corner', 'job description': 'head'},
        { 'id':4,'d_name ':'balochi ','location': ' right side','jobdescriptio': 'head'},
    ]
    department_names_data = [
        {'id': 0, 'name': 'Computer Science'},
        {'id': 1, 'name': 'chemistry'},
        {'id': 2, 'name': 'Balochi'},
        {'id': 3, 'name': 'Sociology'},
        {'id': 4, 'name': 'management science'},
    ]



    departments_data = [dict(department_details, **department_names) for department_details, department_names in zip(department_details_data, department_names_data)]
    return render(request, 'department_list.html', {'departments': departments_data})
