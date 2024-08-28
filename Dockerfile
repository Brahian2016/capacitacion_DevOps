# Usa la imagen base de Python 3.12 más ligera
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /opt/python-api/

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la API al contenedor
COPY main.py .

# Expone el puerto 8000 para acceder al API
EXPOSE 8000

# Define el comando para ejecutar la API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
