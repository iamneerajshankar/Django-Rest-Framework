from api.models import Employee, ApiType
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'emp_code', 'salary', 'band', 'department', 'location', 'emp_type', 'email']


class ApiTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiType
        fields = ['id', 'api_name', 'desc', 'test_link1', 'test_link2']