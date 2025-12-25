from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=150)
    roll_no = models.CharField(max_length=30, blank=True, null=True)
    ppt_file = models.FileField(upload_to="student_ppts/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
