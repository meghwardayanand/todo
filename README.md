<details>
<summary>

# Steps Taken During Development
</summary>

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

</details>

<hr />

<details>
<summary>

# Steps To Use Run This Project
</summary>

## Step 01: Clone the repository
1. Execute `git clone "https://github.com/meghwardayanand/todo"`
2. Execute `cd todo/`

## Step 02: Create & Activate Virtual Environment
1. Execute `pip install virtualenv` command to install virtual environment manager.
2. Execute `virtualenv .env` command to create a virtual environment with name `.env`.
3. Execute `source .env/bin/activate` to activate the environment.

## Step 03: Install Dependencies
1. Execute `pip install --upgrade pip`
2. Execute `pip install -r requirements.txt`

## Step 04: Setup PostgreSQL Database with following Configurations
<code>
    DATABASE_NAME = 'postgres'
    DATABASE_USER = 'postgres'
    DATABASE_PASSWORD = 'postgres'
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = 5432
</code>

## Step 05: Move to "backend" Directory.
1. Execute `cd backend`

## Step 06: Migrate & Create Super User
1. Execute `python manage.py migrate`
2. Execute `python manage.py createsuperuser`
3. Enter Username
4. Enter Email
5. Enter Password & Confirmation Password

## Step 07: Run Development Server
* Execute `python manage.py runserver`

## Step 08: Visit URLs
1. `http://localhost:8000/users/v1/sigin/` to Sign in which will redirect to `Swagger API Documentation`.
2. `http://localhost:8000/admin` and Enter super user's credentials created in "Step 06" to check admin panel.

## Step 09: Play with APIs/Endpoints.

</details>

<hr />

<details open>
<summary>

# API Documentation
</summary>

**Base URL:** `http://localhost:8000` (Add this base url before appending any of the following urls/endpoints.)  
**Consumes/Accepts:** `application/json`  
**Produces/Returns:** `application/json`  

---

## Authentication

### POST `/api-token-auth/`
Request a token for Basic authentication.
* **Request Body:**
  ```json
  {
    "username": "<string>",
    "password": "<string>"
  }
  ```
* **Response (201):**
  ```json
  {
    "token": "<string>"
  }
  ```
---

## TODO APP

### GET `/todos/v1/todos/`
Retrieve a list of all todo items.
* **Response (200):**
  ```json
  [
    {
      "id": 1,
      "title": "<string>",
      "description": "<string>",
      "created_at": "<date-time>",
      "updated_at": "<date-time>",
      "status": "C|I|F",
      "owner": 123
    }
  ]
  ```

### POST `/todos/v1/todos/`
Create a new todo item.
* **Request Body:**
  * `title` is required
  * `description` is required  

  ```json
  {
    "title": "<string>",
    "description": "<string>",
    "created_at": "<date-time>",
    "updated_at": "<date-time>",
    "status": "C|I|F",
    "owner": 123
  }
  ```
* **Response (201):**
  ```json
  {
    "id": 1,
    "title": "<string>",
    "description": "<string>",
    "created_at": "<date-time>",
    "updated_at": "<date-time>",
    "status": "C|I|F",
    "owner": 123
  }
  ```

### GET `/todos/v1/todos/{id}/`
Retrieve a specific todo item by its ID.
* **Path Parameter:**
  * `id` (integer, required): A unique integer value identifying this todo item.
* **Response (200):**
  ```json
  {
    "id": 1,
    "title": "<string>",
    "description": "<string>",
    "created_at": "<date-time>",
    "updated_at": "<date-time>",
    "status": "C|I|F",
    "owner": 123
  }
  ```

### PUT `/todos/v1/todos/{id}/`
Update a specific todo item.
* **Path Parameter:**
  * `id` (integer, required): A unique integer value identifying this todo item.
* **Request Body:**
  * `title` is required
  * `description` is required  

  ```json
  {
    "title": "<string>",
    "description": "<string>",
    "created_at": "<date-time>",
    "updated_at": "<date-time>",
    "status": "C|I|F",
    "owner": 123
  }
  ```
* **Response (200):**
  ```json
  {
    "id": 1,
    "title": "<string>",
    "description": "<string>",
    "created_at": "<date-time>",
    "updated_at": "<date-time>",
    "status": "C|I|F",
    "owner": 123
  }
  ```

### DELETE `/todos/v1/todos/{id}/`
Delete a specific todo item.
* **Path Parameter:**
  * `id` (integer, required): A unique integer value identifying this todo item.
* **Response (204):** No content.

---

## USERS APP

### POST `/users/v1/signin/`
Sign in an existing user.
* **Request Body:**
  * `username` is required
  * `password` is required  

  ```json
  {
    "username": "<string>",
    "password": "<string>"
  }
  ```
* **Response (200):**
  ```json
  {
    "username": "<string>",
    "token": "<string>"
  }
  ```

### POST `/users/v1/signout/`
Sign out the current user.
* **Response (201):** No content.
OR
* **Response (200):**
  ```json
    {
        "message": "Logged out successfully!"
    }
  ```

### POST `/users/v1/signup/`
Register a new user.
* **Request Body:**
  * `username` is required
  * `password` is required  
  * `confirm_password` is required
  * `password` and `confirm_password` should match.   

  ```json
  {
    "username": "<string>",
    "password": "<string>",
    "confirm_password": "<string>"
  }
  ```
* **Response (201):**
  ```json
  {
    "username": "<string>",
    "token": "<string>"
  }
  ```

</details>
