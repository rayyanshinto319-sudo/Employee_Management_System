# Employee Management System — Django

A full-featured Employee Management System built with Django, covering all 9 pages from the design mockup.

## Pages

| # | Page | URL |
|---|------|-----|
| 1 | Register | `/register/` |
| 2 | Login | `/login/` |
| 3 | Dashboard (Employee List) | `/dashboard/` |
| 4 | Add Employee | `/employee/add/` |
| 5 | Employee Profile | `/employee/<id>/` |
| 6 | Edit Employee | `/employee/<id>/edit/` |
| 7 | Delete Confirmation | `/employee/<id>/delete/` |
| 8 | Change Password | `/change-password/` |
| 9 | Logout Success | `/logout-success/` |

## Quick Start

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` contains:
- `Django>=4.2`
- `Pillow>=10.0`  (for profile image uploads)

### 3. Apply migrations

```bash
python manage.py migrate
```

### 4. Create a superuser (optional, for `/admin/`)

```bash
python manage.py createsuperuser
```

### 5. Run the development server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** — you'll be redirected to the login page.

---

## Project Structure

```
employee_management_system/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── employees/
│   ├── migrations/
│   ├── static/employees/css/style.css
│   ├── templates/employees/
│   │   ├── base.html
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── add_employee.html
│   │   ├── employee_detail.html
│   │   ├── edit_employee.html
│   │   ├── delete_employee.html
│   │   ├── change_password.html
│   │   └── logout.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── media/                  # uploaded profile images (auto-created)
├── manage.py
└── requirements.txt
```

## Features

- **Authentication** — register, login with "remember me", logout
- **Employee CRUD** — create, read, update, delete employees
- **Profile images** — upload and display employee photos
- **Search** — search employees by name, department, or email
- **Change password** — secured with `update_session_auth_hash`
- **Flash messages** — success/error feedback on all actions
- **Responsive design** — works on desktop and mobile
- **Django admin** — manage everything at `/admin/`
