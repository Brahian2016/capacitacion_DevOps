"""
Este módulo se encarga de la conexión a una base de datos MongoDB, utilizando variables de entorno 
para configurar el host y el puerto, además de manejar los errores de conexión de manera adecuada.
"""

# Importaciones de librerías estándar
import os
import logging

# Importaciones de librerías externas
from pymongo import MongoClient
from fastapi import HTTPException

# Configuración del logging
logger = logging.getLogger(__name__)

# Variables de conexión
MONGODB_HOST = os.getenv("MONGODB_HOST", "localhost")
MONGODB_PORT = os.getenv("MONGODB_PORT", "27017")

# Inicializar conexión a MongoDB
client = None
collection = None

def connect_to_mongo():
    """
    Establece una conexión con la base de datos MongoDB utilizando los valores 
    de las variables de entorno MONGODB_HOST y MONGODB_PORT. 
    Si la conexión falla, lanza un HTTPException.

    Retorna:
    - Conexión activa a la base de datos y asigna la colección `listas_no_ordenadas`.
    """
    global client, collection
    try:
        client = MongoClient(f'mongodb://{MONGODB_HOST}:{MONGODB_PORT}/')
        db = client.python_app
        collection = db.listas_no_ordenadas
        logger.info("Conexión a MongoDB exitosa")
    except Exception as e:
        logger.error(f"Error al conectar a MongoDB: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")