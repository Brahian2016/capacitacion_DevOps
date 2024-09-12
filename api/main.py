from fastapi import FastAPI, Query
from typing import List
from datetime import datetime
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import os
import uuid

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Conexión a MongoDB utilizando variables de entorno para el host y el puerto.
MONGODB_HOST = os.getenv("MONGODB_HOST", "localhost")
MONGODB_PORT = os.getenv("MONGODB_PORT", "27017")

cliente = MongoClient(f'mongodb://{MONGODB_HOST}:{MONGODB_PORT}/')
db = cliente.python_app
collection = db.listas_no_ordenadas

@app.get("/lista-ordenada", response_class=JSONResponse)
def ordenar_lista(
    lista_no_ordenada: List[int] = Query(
        ..., description="Lista de números no ordenados que se desea ordenar"
        , alias="lista-no-ordenada"
    )
) -> JSONResponse:
    """
    Endpoint para ordenar una lista de números.

    Args:
        lista_no_ordenada (List[int]): Lista de números enteros que se deben ordenar.
    """
    # Ordenar la lista recibida
    lista_ordenada = sorted(lista_no_ordenada)

    # Obtener la hora actual en formato "YYYY-MM-DD HH:MM:SS"
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Crear la respuesta en formato JSON
    response = {"hora_sistema": hora_actual, "lista_ordenada": lista_ordenada}

    return JSONResponse(content=response, media_type="application/json")


@app.get("/healthcheck")
def healthcheck() -> str:
    """
    Endpoint para verificar el estado de la API.
    """
    return "OK"

@app.get("/guardar-lista-no-ordenada", response_class=JSONResponse)
def guardar_lista_no_ordenada(
    lista_no_ordenada: List[int] = Query(..., alias="lista-no-ordenada")
):
    lista_ordenada = sorted(lista_no_ordenada)
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_id = str(uuid.uuid4())

    # Guardar la información en MongoDB
    document = {
        "id": unique_id,
        "hora_sistema": hora_actual,
        "lista_no_ordenada": lista_no_ordenada,
        "lista_ordenada": lista_ordenada
    }
    collection.insert_one(document)

    response = {"msg": f"La lista ordenada fue guardada con el id: {unique_id}"}
    return JSONResponse(content=response)
