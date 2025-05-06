# STEPS

## Step 00: Install Python
1. Install as per instructions at `https://www.python.org/downloads/`.
2. Check Python version with command `python --version`.

## Step 01: Set up Environment
1. Execute `pip install virtualenv` command to install virtual environment manager.
2. Execute `virtualenv .env` command to create a virtual environment with name `.env`.
3. Execute `source .env/bin/activate` to activate the environment.

## Step 02: Install Packages & Dependencies
1. Update pip with command `python -m pip install --upgrade pip`.
2. Install Django with command `pip install "Django>=4.0"` and verify with command `django-admin --version`.
3. Install Django REST Framework with command `pip install "djangorestframework>=3.12"` and verify with command `pip show djangorestframework`.
4. Install Markdown with command `pip install markdown`.
5. Install Django Filter with command `pip install django-filter`.
6. Install Debug Toolbar with command `pip install django-debug-toolbar`.
7. Install pytest with command `pip install -U "pytest>=8.0"` and verify with command `pytest --version`.
8. Install postgresql with command `brew install postgresql@17`.
9. Add path using command `echo 'export PATH="/Library/PostgreSQL/17/bin:$PATH"' >> ~/.zshrc`.
10. Verify postgresql version with command `psql --version` or `postgres --version`.
11. Install Psycopg2 with command `pip install psycopg2-binary` to use postgresql database.
12. Use command `pip freeze > requirements.txt` to add installed packages & their versions in `requirements.txt` file.

## Step 03: Setup Django Project
1. Create project with command `django-admin startproject "backend"`.
2. Change directory to project directory with command `cd backend`.
3. Execute `python manage.py makemigrations` to create migration files.
4. Execute `python manage.py migrate` to apply migrations to the database.
5. Execute `python manage.py runserver` to start the local server.
6. Access `http://127.0.0.1:8000/` to verify the project is working fine.

## Step 04: Add Todo App
1. Create a new app in the project with command `python manage.py startapp todo`.
2. Create `urls.py` file in `todo` directory and setup urls.
3. Register app in `settings.py` file.
4. Create superuser with command `python manage.py createsuperuser` and provide username, password, and confirm password.
5. Start server and verify.
