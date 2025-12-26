from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # 🔥 ROOT URL
    path("upload/", views.upload_student, name="upload_student"),
    path("login/", views.employee_login, name="employee_login"),
    path("dashboard/", views.employee_dashboard, name="employee_dashboard"),
    path("logout/", views.employee_logout, name="employee_logout"),
]
