#!/bin/bash

# Eliminar red Docker si existe
if docker network ls | grep -q mongodb-net; then
  echo "Eliminando red Docker mongodb-net..."
  docker network rm mongodb-net
fi

# Crear la red Docker
echo "Creando red Docker mongodb-net..."
docker network create mongodb-net

# Eliminar contenedor MongoDB si existe
if docker ps -a | grep -q mongodb; then
  echo "Eliminando contenedor MongoDB..."
  docker rm -f mongodb
fi

# Correr MongoDB en un contenedor
echo "Iniciando contenedor MongoDB..."
docker run -d --name mongodb --network mongodb-net -p 27017:27017 mongo:latest

# Eliminar contenedor API si existe
if docker ps -a | grep -q python-api; then
  echo "Eliminando contenedor python-api..."
  docker rm -f python-api
fi

# Construir la imagen Docker para la API
echo "Construyendo imagen Docker python-api..."
docker build -t python-api .

# Correr el contenedor de la API con MongoDB
echo "Iniciando contenedor python-api..."
docker run -d --name python-api --network mongodb-net -e MONGODB_HOST=mongodb -e MONGODB_PORT=27017 -p 8000:8000 python-api
