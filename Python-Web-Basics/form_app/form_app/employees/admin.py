from django.contrib import admin

from form_app.employees.models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'egn', 'job_title', 'company', 'department')
    ordering = ['id',]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
