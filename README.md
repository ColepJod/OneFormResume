# Resume Builder

> Simple Django-based resume and portfolio builder with user authentication, resume CRUD, and PDF download.

## Project overview

This repository contains a Django web application that lets users register, create and edit a personal resume, publish an online portfolio page, and download the resume as a PDF.

Key components
- **Apps:** `accounts` (registration/login) and `resume` (resume model, forms, views)
- **Database:** SQLite (`db.sqlite3`)
- **Templates:** project-level `templates/` and app templates in `templates/resume/` and `templates/accounts/`
- **Static files:** served from the `static/` directory

## Notable files
- `manage.py` — Django management entrypoint
- `resume_project/settings.py` — Django settings (project configured with Django 5.2.4 metadata)
- `resume/models.py` — `Resume` model (one-to-one with `User`)
- `resume/forms.py` — `ResumeForm` ModelForm used for create/edit
- `resume/views.py` — views: `home_view`, `dashboard_view`, `resume_create_view`, `resume_edit_view`, `portfolio_view`
- `accounts/forms.py` — `CustomUserCreationForm` used for registration
- Templates: `templates/base.html`, `templates/home.html`, `templates/resume/portfolio.html`, `templates/resume/resume_form.html`, `templates/resume/dashboard.html`

## Features
- User registration, login, logout
- Create, edit, and store a single resume per user
- Online portfolio pages generated from resume data
- Skill parsing (comma-separated skills rendered as tags)
- PDF download link in the portfolio template (view/URL for `download_pdf` referenced in templates)

## Requirements
- Python 3.10+ (recommended)
- Django (project header indicates generated with Django 5.2.4). Install a compatible Django version, for example:

```powershell
python -m pip install "django>=5.2,<6"
```

If you prefer pinning to the exact version used when the project was created:

```powershell
python -m pip install django==5.2.4
```

Add any additional packages you use (PDF tools, etc.) to a `requirements.txt` if needed.

## Setup (Windows)
1. Create and activate a virtual environment:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1   # PowerShell
# or: venv\Scripts\activate   # cmd.exe
```

2. Install Django (and other dependencies):

```powershell
python -m pip install --upgrade pip
python -m pip install "django>=5.2,<6"
```

3. Run migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Common commands
- Run tests:

```powershell
python manage.py test
```

- Make and apply migrations (if you modify models):

```powershell
python manage.py makemigrations
python manage.py migrate
```

## URL names used in templates/views
- `home`, `dashboard`, `login`, `logout`, `register`, `portfolio`, `resume_create`, `resume_edit`, `download_pdf`

(These names are referenced from templates and views — check `resume_project/urls.py`, `accounts/urls.py`, and `resume/urls.py` for exact patterns.)

## Development notes
- Templates live in `templates/` and use `base.html` for layout. Static CSS is in `static/css/style.css`.
- The `Resume` model enforces one resume per user via a `OneToOneField(User)` in `resume/models.py`.
- The `ResumeForm` excludes the `user` field (the view sets it automatically).
- If PDF download is required, ensure the corresponding view and any third-party PDF library (like `WeasyPrint`, `xhtml2pdf`, or `reportlab`) are installed and configured.

## Next steps (suggested)
- Add a `requirements.txt` listing exact dependency versions: `pip freeze > requirements.txt` after installing.
- Implement or confirm the `download_pdf` view and add tests around resume creation and portfolio rendering.
- Add deployment notes and secrets handling (don't leave `DEBUG = True` or hard-coded secret keys in production)
