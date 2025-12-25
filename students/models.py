from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=50)
    ppt = models.FileField(upload_to="student_ppts/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
