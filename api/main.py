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

# Importaciones de módulos internos
from db.mongodb import connect_to_mongo, collection
from models.document import Document

app = FastAPI()

# Conectar a MongoDB
connect_to_mongo()


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
    """
    Endpoint para guardar una lista no ordenada en la base de datos.
    """
    lista_ordenada = sorted(lista_no_ordenada)
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_id = str(uuid.uuid4())

    document = Document(
        id=unique_id,
        hora_sistema=hora_actual,
        lista_no_ordenada=lista_no_ordenada,
        lista_ordenada=lista_ordenada,
    )

    collection.insert_one(document.to_dict())

    response = {"msg": f"La lista ordenada fue guardada con el id: {unique_id}"}
    return JSONResponse(content=response)


@app.get("/healthcheck")
def healthcheck() -> str:
    """
    Endpoint para verificar el estado de la API.
    """
    return "OK"
