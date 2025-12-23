#!/usr/bin/env python
import os
import django
from django.core.files import File

# 1️⃣ Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # replace 'mysite' with your project folder

# 2️⃣ Setup Django
django.setup()

# 3️⃣ Import your model
from students.models import Student

# 4️⃣ Folder where your local files are stored
LOCAL_FOLDER = "C:/Users/Home/Downloads/student_files/"

# 5️⃣ Loop through all students
for student in Student.objects.all():
    # Skip if already has a Cloudinary file
    if student.ppt_file and student.ppt_file.url.startswith("https://res.cloudinary.com/"):
        continue

    # Get the local filename
    local_filename = os.path.basename(student.ppt_file.name) if student.ppt_file else None
    if not local_filename:
        print(f"Skipping {student.name} — no local file recorded")
        continue

    # Build the full local path
    file_path = os.path.join(LOCAL_FOLDER, local_filename)

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File not found for {student.name}: {file_path}")
        continue

    # Open and save to Cloudinary
    with open(file_path, "rb") as f:
        student.ppt_file.save(local_filename, File(f))

    student.save()
    print(f"✅ Uploaded {student.name} -> {student.ppt_file.url}")
