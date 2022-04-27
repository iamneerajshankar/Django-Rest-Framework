from django.contrib import admin
from Validate.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', 'roll', 'admission_date']
