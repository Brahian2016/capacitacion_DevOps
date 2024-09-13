# Capacitación DevOps

Esta es una aplicación web construida con **FastAPI** que proporciona un endpoint para ordenar una lista de números enteros y un endpoint de verificación de estado. Además, permite guardar listas no ordenadas en una base de datos **MongoDB**.

## Instalación

Para construir y ejecutar la aplicación, sigue estos pasos:

**1. Ingresar al modulo de la aplicación**:
```bash
cd api
```

**2. Crear la red para MongoDB**:

```bash
docker network create mongodb-net
```

**3. Correr MongoDB en un contenedor**:

```bash
docker run -d --name mongodb --network mongodb-net -p 27017:27017 mongo:latest
```

**4. Construir la imagen Docker para la API**:

```bash
docker build -t python-api .
```

**5. Correr el contenedor de la API con MongoDB**:

```bash
docker run -d --name python-api --network mongodb-net -e MONGODB_HOST=mongodb -e MONGODB_PORT=27017 -p 8000:8000 python-api
```

## Uso de la API

La API tiene tres endpoints disponibles:

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
  ```


### 2. Guardar lista no ordenada
- **Endpoint**: `/guardar-lista-no-ordenada`
- **Método**: `GET`
- **Parámetros**:
  - `lista-no-ordenada`: Lista de números enteros no ordenada a guardar.  
    (Ejemplo: `?lista-no-ordenada=5&lista-no-ordenada=2&lista-no-ordenada=9`)
- **Respuesta**:
  ```json
  {
    "msg": "La lista ordenada fue guardada con el id: 9743ee94-6690-11ef-a4d5-089df4cb467e"
  }
  ```

### 3. Verificación de estado
- **Endpoint**: `/healthcheck`
- **Método**: `GET`
- **Respuesta**:
  ```text
  OK
  ```

## Ejemplos de Uso

Puedes probar la API utilizando `curl` o cualquier herramienta para realizar peticiones HTTP, como Postman.


### 1. Ordenar lista de números

```bash
curl "http://localhost:8000/lista-ordenada?lista-no-ordenada=3&lista-no-ordenada=1&lista-no-ordenada=2"
```

### 2. Guardar lista no ordenada

```bash
curl "http://localhost:8000/guardar-lista-no-ordenada?lista-no-ordenada=5&lista-no-ordenada=2&lista-no-ordenada=9"
```

### 3. Verificación de estado
```bash
curl "http://localhost:8000/healthcheck"
```

### Visualizar los datos en MongoDB Compass

Para visualizar las listas guardadas, usa **MongoDB Compass**. Conéctate a la base de datos en la siguiente dirección: `mongodb://localhost:27017`, Luego, selecciona la base de datos `python_app` y la colección `listas_no_ordenadas` para ver los datos almacenados.