# Use una imagen base de Python
FROM python:3.9-slim

# Establece la variable de entorno PYTHONUNBUFFERED a 1 para evitar problemas con la salida
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido de la carpeta del proyecto al contenedor
COPY . /app/

# Exponer el puerto 8080 para que Gunicorn escuche
EXPOSE 8080

# Ejecutar Gunicorn para servir la aplicación Django
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "config.wsgi:application"]
