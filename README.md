# Capacitación DevOps

Esta es una aplicación web construida con FastAPI que proporciona un endpoint para ordenar una lista de números enteros y un endpoint de verificación de estado.

## Instalación

Para construir y ejecutar la aplicación, sigue estos pasos:

**1. Construye la imagen de Docker**:

```
docker build -t python-api .
```

**2. Ejecuta el contenedor**:

```
docker run -d -p 8000:8000 python-api
```

## Uso de la API

La API tiene dos endpoints disponibles:

### 1. Ordenar lista de números
- **Endpoint**: `/lista-ordenada`
- **Método**: `GET`
- **Parámetros**:
  - `lista-no-ordenada`: Lista de números enteros que se desea ordenar.  
    (Ejemplo: `?lista-no-ordenada=3&lista-no-ordenada=1&lista-no-ordenada=2`)
- **Respuesta**:
  ```json
  {
    "hora_sistema": "YYYY-MM-DD HH:MM:SS",
    "lista_ordenada": [1, 2, 3]
  }

### 2. Verificación de estado
- **Endpoint**: `/healthcheck`
- **Método**: `GET`
- **Respuesta**:
  ```text
  OK

## Ejemplos de Uso

Puedes probar la API utilizando `curl` o cualquier herramienta para realizar peticiones HTTP, como Postman.


### 1. Ordenar lista de números

```bash
curl "http://localhost:8000/lista-ordenada?lista-no-ordenada=3&lista-no-ordenada=1&lista-no-ordenada=2"
```

### 2. Verificación de estado
```bash
curl "http://localhost:8000/healthcheck"
```