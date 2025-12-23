from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import StudentForm
from .models import Student

# 🏠 Home page — list of latest uploads (50 latest)
def home(request):
    students = Student.objects.order_by('-created_at')[:50]
    return render(request, 'students/home.html', {'students': students})

# 📤 Student file upload (saves to Cloudinary)
def upload_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()  # automatically uses Cloudinary storage
            messages.success(request, f"{student.name}'s file uploaded successfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error uploading the file. Please try again.")
    else:
        form = StudentForm()
    return render(request, 'students/upload.html', {'form': form})

# 👨‍💼 Employee login
def employee_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee_dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'students/employee_login.html')

# 🧾 Employee dashboard (shows all uploads)
def employee_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('employee_login')

    uploads = Student.objects.all().order_by('-created_at')
    return render(request, 'students/employee_dashboard.html', {'uploads': uploads})

# 🚪 Employee logout
def employee_logout(request):
    logout(request)
    return redirect('employee_login')
