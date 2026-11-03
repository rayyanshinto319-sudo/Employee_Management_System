from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Employee
from .forms import RegisterForm, EmployeeForm, CustomPasswordChangeForm


# ──────────────────────────────────────────────
# 1. Home / Landing (redirects based on auth)
# ──────────────────────────────────────────────
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


# ──────────────────────────────────────────────
# 1. Register Page
# ──────────────────────────────────────────────
def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome aboard.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()

    return render(request, 'employees/register.html', {'form': form})


# ──────────────────────────────────────────────
# 2. Login Page
# ──────────────────────────────────────────────
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember_me')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if not remember:
                request.session.set_expiry(0)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'employees/login.html')


# ──────────────────────────────────────────────
# 3. Dashboard – Employee List
# ──────────────────────────────────────────────
@login_required
def dashboard(request):
    query = request.GET.get('q', '')
    employees = Employee.objects.all()
    if query:
        employees = employees.filter(
            Q(name__icontains=query) |
            Q(department__icontains=query) |
            Q(email__icontains=query)
        )
    return render(request, 'employees/dashboard.html', {
        'employees': employees,
        'query': query,
    })


# ──────────────────────────────────────────────
# 4. Add Employee Page
# ──────────────────────────────────────────────
@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EmployeeForm()

    return render(request, 'employees/add_employee.html', {'form': form})


# ──────────────────────────────────────────────
# 5. Single Employee Profile Page
# ──────────────────────────────────────────────
@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})


# ──────────────────────────────────────────────
# 6. Edit Employee Page
# ──────────────────────────────────────────────
@login_required
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully!')
            return redirect('employee_detail', pk=pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/edit_employee.html', {'form': form, 'employee': employee})


# ──────────────────────────────────────────────
# 7. Delete Employee Confirmation
# ──────────────────────────────────────────────
@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('dashboard')

    return render(request, 'employees/delete_employee.html', {'employee': employee})


# ──────────────────────────────────────────────
# 8. Change Password Page
# ──────────────────────────────────────────────
@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'employees/change_password.html', {'form': form})


# ──────────────────────────────────────────────
# 9. Logout
# ──────────────────────────────────────────────
def logout_view(request):
    logout(request)
    return redirect('logout_success')


def logout_success(request):
    return render(request, 'employees/logout.html')
