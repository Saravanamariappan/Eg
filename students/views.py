from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Student


# =========================
# Home – Student List
# =========================
def home(request):
    students = Student.objects.all().order_by('-created_at')
    return render(request, 'students/home.html', {
        'students': students
    })


# =========================
# Upload Student PPT
# =========================
def upload_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        ppt_file = request.FILES.get('ppt_file')

        student = Student.objects.create(
            name=name,
            roll_no=roll_no,
            ppt_file=ppt_file
        )

        return render(request, 'students/upload_success.html', {
            'student': student
        })

    return render(request, 'students/upload_form.html')


# =========================
# Employee Login
# =========================
def employee_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('employee_dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'students/employee_login.html')


# =========================
# Employee Dashboard
# =========================
@login_required(login_url='employee_login')
def employee_dashboard(request):
    uploads = Student.objects.all().order_by('-created_at')
    return render(request, 'students/employee_dashboard.html', {
        'uploads': uploads
    })


# =========================
# Employee Logout
# =========================
def employee_logout(request):
    logout(request)
    return redirect('employee_login')
