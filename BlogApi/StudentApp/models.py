from django.db import models


# **************************** Student Model class ********************************
class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    roll = models.IntegerField()
    admission_date = models.DateField()

