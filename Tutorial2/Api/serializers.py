from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    grade = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    
    class Meta:
        model = Student
        fields = ['first_name','last_name','grade','age']

    # def validate(self, attrs):
    #     print()
        
    #     if attrs.get('age') == 0 :
    #         raise serializers.ValidationError({'age' : 'Please enter right age'})
       
    #     return super(StudentSerializer, self).validate(attrs)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.grade = validated_data.get('grade',instance.grade)
        instance.age = validated_data.get('age',instance.age)
        instance.save()
        return instance 