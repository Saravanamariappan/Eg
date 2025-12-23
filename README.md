# Django + Cloudinary Sample Project


This is a minimal sample Django project demonstrating file uploads to Cloudinary, storing file URLs in MySQL, and a simple frontend for upload and list.


## What's included


- `mysite/` - Django project
- `students/` - Django app with Student model, upload form, views, and templates
- `sample_data.sql` - SQL commands to create database + sample rows
- `.env.example` - environment variable template (DO NOT commit secrets)
- `requirements.txt` - Python dependencies


## Quick Setup (Local testing)

1. Install Python 3.10+ and MySQL server locally.
2. Create a Python virtualenv and activate it:
```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```
3. Copy `.env.example` to `.env` and fill values (especially Cloudinary credentials).

4. Edit `mysite/settings.py` if necessary; settings already read from environment variables.

5. Create MySQL database (or run `sample_data.sql`):
```sql
-- in MySQL client
CREATE DATABASE studentdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- then update .env with DB credentials and run migrations below
```

6. Run migrations and start the server:
```bash
python manage.py migrate
python manage.py runserver
```

7. Open `http://127.0.0.1:8000/` to see the upload page.


## Cloudinary Setup (short)
1. Sign up at https://cloudinary.com and get CLOUD_NAME, API_KEY, API_SECRET.
2. Put them in `.env` as shown in `.env.example`.
3. The project uses `django-cloudinary-storage` as DEFAULT_FILE_STORAGE so when you upload via Django forms the file will go to Cloudinary and the model stores the URL.


## How upload + retrieval works (overview)
- User uploads PPT via Django form
- Django uses Cloudinary storage backend to send file to Cloudinary
- The `Student` model stores the resulting `ppt_file.url` (a URL pointing to Cloudinary)
- When listing students, templates show link to the file URL which downloads from Cloudinary


## sample_data.sql
- Includes example SQL to create `students` table and insert sample rows. Use it if you want to seed MySQL directly.


## Notes
- This is a starter template. Replace secret values with real ones and secure `.env` in production.
- For production hosting, consider Render / Railway / PlanetScale for DB and connect Cloudinary for file storage.
