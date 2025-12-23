from django.contrib import admin
from django.urls import path
from students import views  # your views.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('upload/', views.upload_student, name='upload_student'),

    # Employee login system
    path('employee/login/', views.employee_login, name='employee_login'),
    path('employee/dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('employee/logout/', views.employee_logout, name='employee_logout'),
]

# ✅ Add this part at the bottom
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
