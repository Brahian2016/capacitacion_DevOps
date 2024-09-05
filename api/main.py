from fastapi import FastAPI, Query
from typing import List
from datetime import datetime
from fastapi.responses import JSONResponse

# Inicialización de la aplicación FastAPI
app = FastAPI()


@app.get("/lista-ordenada", response_class=JSONResponse)
def ordenar_lista(
    lista_no_ordenada: List[int] = Query(
        ..., description="Lista de números no ordenados que se desea ordenar"
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
