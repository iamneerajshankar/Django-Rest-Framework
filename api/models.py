from django.db import models

EMP_TYP_CHOICE = (
    ('Permanent', 'Permanent'),
    ('Temporary', 'Temporary'),
    ('Internship', 'Internship')
)

EMP_BAND_CHOICE = (
    ('S0', 'S0'),
    ('S1', 'S1'),
    ('S2', 'S2'),
    ('S3', 'S3'),
    ('S4', 'S4'),
    ('S5', 'S5')
)

DEPT_CHOICE = [
    ('DEV', 'Development'),
    ('FIN', 'Finance'),
    ('HR', 'Human Resource'),
    ('TA', 'Talent Acquisition'),
    ('Admin', 'Administration')
]


class Employee(models.Model):
    name = models.CharField(verbose_name="Employee Name", max_length=50)
    emp_code = models.IntegerField(verbose_name="Employee Code")
    salary = models.IntegerField(verbose_name="Salary")
    band = models.CharField(verbose_name="Band Level", choices=EMP_BAND_CHOICE, default='S0', max_length=50)
    department = models.CharField(verbose_name="Department", choices=DEPT_CHOICE, default='Development', max_length=50)
    location = models.CharField(verbose_name="Job Location", max_length=50)
    emp_type = models.CharField(verbose_name="Employment Type", choices=EMP_TYP_CHOICE, default="Permanent", max_length=50)
    email = models.EmailField(verbose_name="Email Address", max_length=50)


class ApiType(models.Model):
    api_name = models.CharField(verbose_name='API Type', help_text='Title for the type of API',max_length=200)
    desc = models.TextField(verbose_name='Description', help_text='Describe a little about this API')
    test_link1 = models.URLField(verbose_name='API Link 1', help_text='Link to test the API', max_length=250)
    test_link2 = models.URLField(verbose_name='API Link 2', help_text='Link to test the API', max_length=250)

