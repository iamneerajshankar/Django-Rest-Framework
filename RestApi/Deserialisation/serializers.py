from rest_framework import serializers
from Deserialisation.models import Student

class StudentDeSerialization(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    roll = serializers.CharField(max_length=70)
    marks = serializers.IntegerField()
    pass_date = serializers.DateField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)