from django.db import models

# EMPLOYEE MODEL

class EmployeeModel(models.Model):
    employee_number = models.CharField(max_length=10, unique=True)
    employee_email = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Other fields such as address, phone, etc.

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Attendance Model
class AttendanceModel(models.Model):
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    date = models.DateField()
    entry_time = models.TimeField(default='09:00')  # Default entry time at 9:00 AM
    lunch_time = models.TimeField(default='10:30')  # Default lunch time at 10:30 AM
    exit_time = models.TimeField(default='18:00')  # Default exit time at 6:00 PM
    entry_photo = models.ImageField(upload_to='attendances/%Y/%m/%d/', blank=True, null=True)
    non_attendance = models.BooleanField(default=True)

    # Other fields that may be necessary

    def __str__(self):
        return f'Attendance of {self.employee} on {self.date}'
