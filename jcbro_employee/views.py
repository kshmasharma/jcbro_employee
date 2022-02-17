from django.shortcuts import render, redirect  
from jcbro_employee.form import EmployeeForm  
from jcbro_employee.models import Employee
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.
@csrf_protect

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else :
        form = EmployeeForm()
    return render(request, 'add.html',{'form':form})

def show(request):
    employees = Employee.objects.all()
    return render(request, 'show.html',{'employees':employees})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        try:
            form.save()
            return redirect("/show")
        except:
            pass
    return render(request, 'edit.html',{"employee":employee})

def delete(request, id):
    employee = Employee.objects.get(id = id)
    form = EmployeeForm(request.POST, instance = employee)
    if request.method == 'POST':
        employee.delete()
        return redirect("/show")
    return render(request, 'delete.html', {'employee':employee})