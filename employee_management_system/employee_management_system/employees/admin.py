from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name', 'department', 'email', 'phone', 'salary']
    search_fields = ['name', 'email', 'department']
    list_filter   = ['department']
