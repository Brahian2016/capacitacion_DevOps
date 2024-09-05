# Usa la imagen base de Python 3.12 más ligera (slim)
# para reducir el tamaño de la imagen y mejorar la eficiencia.
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor.
# Todos los comandos posteriores se ejecutarán en este directorio.
WORKDIR /opt/python-api/

# Copia el archivo requirements.txt desde el host al contenedor.
# Este archivo contiene las dependencias necesarias para la aplicación.
COPY api/requirements.txt .

# Ejecuta la instalación de las dependencias listadas en requirements.txt.
# Se usa --no-cache-dir para evitar guardar cachés de paquetes y reducir el tamaño de la imagen final.
RUN pip install --no-cache-dir -r requirements.txt

# Copia el archivo principal de la API FastAPI (main.py) desde el host al contenedor.
# Este archivo contiene la lógica del servidor.
COPY api/main.py .

# Expone el puerto 8000, que es el puerto por defecto donde FastAPI sirve la aplicación.
# Esto permite acceder a la API desde fuera del contenedor.
EXPOSE 8000

# Define el comando para ejecutar la aplicación FastAPI con Uvicorn.
ENTRYPOINT ["uvicorn", "main:app"]

# Define las opciones por defecto para Uvicorn.
# --host 0.0.0.0 permite que el servidor acepte conexiones externas,
# y --port 8000 especifica el puerto en el que el servidor estará escuchando.
CMD ["--host", "0.0.0.0", "--port", "8000"]
