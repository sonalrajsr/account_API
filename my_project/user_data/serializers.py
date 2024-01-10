from rest_framework import serializers
from .models import student_data

class StudentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_data
        fields = '__all__'
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return student_data.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.First_name = validated_data.get('First_name', instance.First_name)
        instance.Last_name = validated_data.get('Last_name', instance.Last_name)
        instance.current_class = validated_data.get('current_class', instance.current_class)
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
