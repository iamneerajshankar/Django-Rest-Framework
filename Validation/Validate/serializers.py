from rest_framework import serializers
from Validate.models import Student


# additional validators
def starts_with_s(value):
    if value[0].lower() == 's':
        raise serializers.ValidationError('Name should not start with S or s')


# ************************** Serializing Student Model ***********************
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[starts_with_s])
    course = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    admission_date = serializers.DateField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # field level validation - to validate single field
    @staticmethod
    def validate_course(value):
        if value == "Bachelor in Commerce":
            raise serializers.ValidationError('Bachelor in Commerce is not admissible')
        return value

    # object level validation - to validate multiple fields
    def validate(self, attrs):
        crs = attrs.get('course')
        rl = attrs.get('roll')
        if crs != "Computer Science Engineering" or rl > 2000:
            raise serializers.ValidationError("Not eligible for training")
        return attrs

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.course = validated_data.get('course', instance.course)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.admission_date = validated_data.get('admission_date', instance.admission_date)
        instance.save()
        return instance
