from django.contrib import admin
from .models import EmployeeModel, AttendanceModel

# Define admin classes if you want to customize the admin interface
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_number', 'first_name', 'last_name']

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['employee', 'date', 'entry_time', 'lunch_time', 'exit_time']

# Register your models with their respective admin classes
admin.site.register(EmployeeModel, EmployeeAdmin)
admin.site.register(AttendanceModel, AttendanceAdmin)
