from rest_framework import serializers
from StudentApp.models import Student


# ************************** Serializing Student Model ***********************
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    course = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    admission_date = serializers.DateField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.course = validated_data.get('course', instance.course)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.admission_date = validated_data.get('admission_date', instance.admission_date)
        instance.save()
        return  instance