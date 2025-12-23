from django.db import models

class Student(models.Model):
    # Basic student details
    name = models.CharField(max_length=150)
    roll_no = models.CharField(max_length=30, blank=True, null=True)

    # Uploaded file (e.g., PPT, PDF, Image)
    ppt_file = models.FileField(upload_to='student_ppts/', blank=True, null=True)

    # Timestamp for record creation
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Display both name and roll number for clarity
        if self.roll_no:
            return f"{self.name} ({self.roll_no})"
        return self.name
