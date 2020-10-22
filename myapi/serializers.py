from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'last_name', 'employee_number']

# class EmployeeSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     employee_number = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Employee.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.id = validated_data.get('id', instance.id)
#         instance.name = validated_data.get('name', instance.name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.employee_number = validated_data.get('employee_number', instance.employee_number)
#         instance.save()
#         return instance
