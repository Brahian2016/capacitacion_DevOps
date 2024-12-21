import os
import time
import logging
import requests
from datetime import datetime

# Configuración del logging
logging.basicConfig(
    filename='/opt/monitor/logs/api-monitor.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Variables de entorno
TARGET_CONTAINER_HOST = os.getenv("TARGET_CONTAINER_HOST", "api-container")
TARGET_CONTAINER_PORT = os.getenv("TARGET_CONTAINER_PORT", 8000)
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 5))
API_URL = f"http://{TARGET_CONTAINER_HOST}:{TARGET_CONTAINER_PORT}/healthcheck"

def monitor_health():
    while True:
        try:
            response = requests.get(API_URL)
            if response.status_code == 200 and response.text == "OK":
                logging.info(f"Se hizo la solicitud al endpoint {API_URL} y devolvió OK")
            else:
                logging.error(f"Se hizo la solicitud al endpoint {API_URL} y devolvió error: Código de estado: {response.status_code}, Respuesta: {response.text}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error al hacer la solicitud al endpoint {API_URL}: {str(e)}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_health()
