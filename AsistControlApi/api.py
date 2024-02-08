from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmployeeModel, AttendanceModel
from .serializers import EmployeeSerializer, AttendanceSerializer

from datetime import date, datetime, time

# registro de empleados
class EmployeeLookup(APIView):
    def post(self, request):
        # Extract data from the request
        employee_number = request.data.get('employee_number')
        employee_email = request.data.get('employee_email')

        # Check if the employee exists
        try:
            employee = EmployeeModel.objects.get(employee_number=employee_number, employee_email=employee_email)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except EmployeeModel.DoesNotExist:
            return Response({"message": "Datos incorrectos"}, status=status.HTTP_404_NOT_FOUND)


# registro de asistencias
class ManageAttendance(APIView):
    def post(self, request):
        # Extraer datos de la solicitud
        employee_number = request.data.get('employee_number')
        photo = request.FILES.get('photo')  # Obtener la foto de la solicitud

        # Obtener el empleado
        try:
            employee = EmployeeModel.objects.get(employee_number=employee_number)
        except EmployeeModel.DoesNotExist:
            return Response("Empleado no encontrado", status=status.HTTP_404_NOT_FOUND)

        # Verificar si ya existe un registro de asistencia para hoy
        today = date.today()
        try:
            attendance = AttendanceModel.objects.get(employee=employee, date=today)
            return Response({"message": "El empleado ya tiene registrada la asistencia para hoy", "entry_time": attendance.entry_time}, status=status.HTTP_400_BAD_REQUEST)
        except AttendanceModel.DoesNotExist:
            pass

        # Obtener la hora actual
        time_now = datetime.now().time()

        # Asignar las horas de entrada, comida y salida
        entry_time = time_now  # Hora de entrada a las 9:00 AM
        lunch_time = time(10, 30)  # Hora de comida a las 10:30 AM
        exit_time = time(18, 0)  # Hora de salida a las 6:00 PM

        # Crear un nuevo registro de asistencia para el empleado
        attendance_data = {
            'employee': employee.id,
            'date': today,
            'entry_time': entry_time,
            'lunch_time': lunch_time,
            'exit_time': exit_time,
            'non_attendance': False,  # Cambiar el estado de non_attendance a False
            'photo': photo  # Guardar la foto en el registro de asistencia
        }
        serializer = AttendanceSerializer(data=attendance_data)
        if serializer.is_valid():
            serializer.save()
            employee_name = f"{employee.first_name} {employee.last_name}"
            # Incluir el nombre del empleado en la respuesta
            response_data = serializer.data
            response_data['employee_name'] = employee_name
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
