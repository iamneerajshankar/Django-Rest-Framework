from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()