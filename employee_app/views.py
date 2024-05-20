from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from datetime import datetime
from .forms import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def index(request):
    return render(request, 'emp_index.html')
def all_emp(request):
    emps = Employee.objects.all()
    return render(request, 'view_all_emp.html', {'emp':emps})


def add_emp(request):
    form = employee_form
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept, role_id = role, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method=='GET':
        return render(request, 'add_emp.html',{'form':form})
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)

#
# def filter_emp(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         dept = request.POST['dept']
#         role = request.POST['role']
#         emps = Employee.objects.all()
#         if name:
#             emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
#         if dept:
#             emps = emps.filter(dept__name__icontains = dept)
#         if role:
#             emps = emps.filter(role__name__icontains = role)
#
#         context = {
#             'emps': emps
#         }
#         return render(request, 'view_all_emp.html', context)
#
#     elif request.method == 'GET':
#         return render(request, 'filter_emp.html')
#     else:
#         return HttpResponse('An Exception Occurred')


# ----------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------API-data-Employee-------------------------------------------------------------------
@api_view(['GET','POST'])
def employee_API(request,format=None):
    # access all data
    # serialize them
    # return Json
    if request.method == 'GET':
        emp_data = Employee.objects.all()
        emp_serialize = employee_serilizer(emp_data,many=True)
        return Response({'employee':emp_serialize.data})
    if request.method == 'POST':
        emp_serialize = employee_serilizer(data=request.data)
        if emp_serialize.is_valid():
            emp_serialize.save()
            return JsonResponse(data={'employee': emp_serialize.data})
        return Response(emp_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def emp_API_details(request,format=None,**kwargs):
    try:
        emp_data = Employee.objects.get(id=kwargs.get('id'))
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        emp_serialize = employee_serilizer(emp_data)
        return Response({'employee': emp_serialize.data})
    if request.method == 'PUT':
        emp_serializer = employee_serilizer(data=request.data,instance=emp_data)
        if emp_serializer.is_valid():
            emp_serializer.save()
            return Response(emp_serializer.data,status=status.HTTP_200_OK)
        return Response(emp_serializer.errors)
    if request.method == 'DELETE':
        emp_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)