#!/bin/bash

# Detener y eliminar los contenedores, redes y volúmenes del perfil 'back' si existen
docker-compose --profile back down

# Eliminar contenedores específicos si aún existen
docker rm -f mongodb python-api api-monitor 2>/dev/null

# Limpiar los directorios de volúmenes montados (logs)
echo "Limpieza del volumen de logs..."
rm -rf ./volumes/logs/*

# Volver a construir y levantar los servicios con el perfil "back"
echo "Reconstruyendo y desplegando servicios..."
docker-compose --profile back up -d --build
