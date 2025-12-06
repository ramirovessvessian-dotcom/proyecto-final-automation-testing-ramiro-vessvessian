import pytest
import requests 
from utils.logger import logger

# Obtener usuario
def test_get_user(url_base, header_request):
    # La URL completa será "https://reqres.in/api/users/2"
    logger.info("Realizando la solicitud GET a {url_base}")
    response = requests.get(f"{url_base}/2", headers=header_request)
    
    logger.info(f"Status code: {response.status_code}")
    # Verifica que la petición fue exitosa (código 200 OK)
    assert response.status_code == 200
    
    data = response.json()
    
    logger.info("Validando el id dentro del usuario")
    # Verifica que el ID del usuario en la respuesta es el esperado
    assert data["data"]["id"] == 2

# Crear usuario
def test_create_user(url_base, header_request):
    payload = {
        "name": "Jose",
        "job": "Profesor"
    }
    
    # Envía una petición POST con los datos (payload) en formato JSON
    response = requests.post(url_base, headers=header_request, json=payload)
    
    # Verifica que la creación fue exitosa (código 201 Created)
    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]

# Eliminar usuario
def test_delete_user(url_base, header_request):
    # La URL completa es la base + "/2"
    # Nota: Los headers no son estrictamente necesarios para esta API, pero se incluyen por consistencia si fueran requeridos.
    response = requests.delete(f"{url_base}/2", headers=header_request) 
    
    # Verifica que la eliminación fue exitosa (código 204 No Content)
    assert response.status_code == 204