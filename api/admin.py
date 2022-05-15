from django.contrib import admin
from api.models import Employee, ApiType
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'emp_code', 'salary', 'band', 'department', 'location', 'emp_type', 'email']


@admin.register(ApiType)
class ApiTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'api_name', 'desc', 'test_link1', 'test_link2']
    fields = ['api_name', 'desc', 'test_link1', 'test_link2']