"""
Este módulo proporciona funciones para conectarse a MongoDB y acceder a la base de datos y colecciones necesarias.

Funciones:
- get_mongo_client: Obtiene una instancia de MongoClient.
- get_db: Obtiene la base de datos 'python_app'.
- get_collection: Obtiene la colección 'listas_no_ordenadas' de la base de datos.
"""

from pymongo import MongoClient
import os


def get_mongo_client() -> MongoClient:
    """
    Obtiene una instancia de MongoClient con la configuración proporcionada a través de variables de entorno.

    Returns:
        MongoClient: Una instancia de MongoClient configurada con el host y el puerto proporcionados.
    """
    host = os.getenv("MONGODB_HOST")
    port = int(os.getenv("MONGODB_PORT"))
    return MongoClient(host, port)


def get_db():
    """
    Obtiene la base de datos 'python_app'.

    Returns:
        Database: La base de datos 'python_app' en MongoDB.
    """
    client = get_mongo_client()
    return client["python_app"]


def get_collection():
    """
    Obtiene la colección 'listas_no_ordenadas' de la base de datos.

    Returns:
        Collection: La colección 'listas_no_ordenadas' de la base de datos 'python_app'.
    """
    db = get_db()
    return db["listas_no_ordenadas"]
