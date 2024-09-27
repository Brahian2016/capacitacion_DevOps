# Capacitación DevOps

Esta es una aplicación web construida con **FastAPI** que proporciona un endpoint para ordenar una lista de números enteros y un endpoint de verificación de estado. Además, permite guardar listas no ordenadas en una base de datos **MongoDB**.

## Instalación

Para construir y ejecutar la aplicación hay 2 formas:

### Alternativa 1:

**1. Ingresar al modulo de la aplicación**:
```bash
cd api
```

**2. Dar permisos al script de bash**:
```bash
chmod +x setup.sh
```

**2. Ejecutar el script de bash**:
```bash
./setup.sh
```

### Alternativa 2:

**1. Ingresar al modulo de la aplicación**:
```bash
cd api
```

### Alternativa 3: Uso de docker-compose
La aplicación también puede levantarse usando `docker-compose`, lo que facilita la creación de un entorno completo con la API y MongoDB conectados a través de una red y con volúmenes para la persistencia de datos.

**Levantar los servicios con Docker Compose:**
```bash
docker-compose --env-file .env.demo --profile api --profile db up -d
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