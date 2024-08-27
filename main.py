from fastapi import FastAPI
from typing import List
from datetime import datetime

app = FastAPI()


@app.get("/lista-ordenada", tags=["lista-ordenada"])
def ordenar_lista(lista_no_ordenada: List[int]):
    lista_ordenada = sorted(lista_no_ordenada)
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"hora_sistema": hora_actual, "lista_ordenada": lista_ordenada}


@app.get("/healthcheck")
def healthcheck():
    return {"response": "OK"}
