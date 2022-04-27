from pyexpat import model
from django.contrib import admin
from Deserialisation.models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'roll', 'marks', 'pass_date')
