from django.urls import path
from .api import EmployeeLookup, ManageAttendance

urlpatterns = [
    path('lookup/', EmployeeLookup.as_view(), name='employee_lookup'),  # URL para la vista de consulta de empleado
    path('attendance/', ManageAttendance.as_view(), name='manage_attendance'),  # URL para la vista de administración de asistencia
]