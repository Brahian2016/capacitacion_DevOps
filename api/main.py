"""
Este módulo define una API con FastAPI que incluye los siguientes endpoints:
- /lista-ordenada: para ordenar una lista de números.
- /guardar-lista-no-ordenada: para guardar una lista no ordenada en la base de datos.
- /healthcheck: para verificar el estado de la API.
"""

# Importaciones de librerías estándar
import os
import uuid
from datetime import datetime
from typing import List

# Importaciones de librerías externas
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import logging

# Importaciones de módulos internos
from db.mongodb import get_collection
from models.document import Document

# Configuración del logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/lista-ordenada", response_class=JSONResponse)
def ordenar_lista(
    lista_no_ordenada: List[int] = Query(
        ...,
        description="Lista de números no ordenados que se desea ordenar",
        alias="lista-no-ordenada",
    )
) -> JSONResponse:
    """
    Endpoint para ordenar una lista de números.
    """
    lista_ordenada = sorted(lista_no_ordenada)
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    response = {"hora_sistema": hora_actual, "lista_ordenada": lista_ordenada}

    return JSONResponse(content=response)


@app.get("/guardar-lista-no-ordenada", response_class=JSONResponse)
def guardar_lista_no_ordenada(
    lista_no_ordenada: List[int] = Query(..., alias="lista-no-ordenada")
) -> JSONResponse:
    try:
        lista_ordenada = sorted(lista_no_ordenada)
        hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        unique_id = str(uuid.uuid4())

        # Obtener la colección de MongoDB
        collection = get_collection()

        # Crear una instancia de Document
        document = Document(
            id=unique_id,
            hora_sistema=hora_actual,
            lista_no_ordenada=lista_no_ordenada,
            lista_ordenada=lista_ordenada,
        )

        if collection is not None:
            # Insertar el documento en la colección
            collection.insert_one(document.to_dict())
            response = {"msg": f"La lista ordenada fue guardada con el id: {unique_id}"}
        else:
            response = {"error": "No se pudo conectar a la base de datos"}
        return JSONResponse(content=response)
    except Exception as e:
        logger.error(f"Error al guardar la lista: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al guardar la lista")


@app.get("/healthcheck")
def healthcheck() -> str:
    """
    Endpoint para verificar el estado de la API.
    """
    return "OK"
