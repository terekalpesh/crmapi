# CMS Project (Django Rest Framework)
- This 'Content Management System' project built with Django and Django Rest Framework.
- It includes user authentication using dj-rest-auth and django-allauth.
- It also include authorization using django-rest-framework permissions.

## Features
- User registration, login, logout.
- Authorization
- CRUD Operations for Posts
- Token-based authentication
- Field-level validation

## Technologies Used
- Django
- Django REST Framework (DRF)
- dj-rest-auth
- django-allauth
- SQLite (default, but can be replaced with any other database)

## Installation
1. **Clone the repositary**

2. **Create and activate virtual environment**
    - python -m venv .venv
    - .venv\scripts\activate

3. **Install the required packages**
    - python -m pip install -r requirements.txt

4. **Migrations**
    - python manage.py makemigrations
    - python manage.py migrate

5. **Create superuser**
    - python manage.py createsuperuser

6. **Run Server**
    - python manage.py runserver


## Endpoints
- api/
- api/<int:pk>/
- api/?search=
- api-auth/
- api/dj-rest-auth/
- api/dj-rest-auth/registration/
- api/dj-rest-auth/login
- admin/