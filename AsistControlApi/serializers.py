from rest_framework import serializers
from .models import EmployeeModel, AttendanceModel

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ['id', 'employee_number', 'employee_email', 'first_name', 'last_name']


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceModel
        fields = ['id', 'employee', 'date', 'entry_time', 'lunch_time', 'exit_time', 'entry_photo']