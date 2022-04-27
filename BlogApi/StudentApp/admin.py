from django.contrib import admin
from StudentApp.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', 'roll', 'admission_date']
