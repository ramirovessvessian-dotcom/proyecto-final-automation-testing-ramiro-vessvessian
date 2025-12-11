# Proyecto de Talento Tech

## Propósito del proyecto

Este proyecto tiene como objetivo automatizar pruebas de UI y de API para el sitio SauceDemo, aplicando practicas como Page Object Model, manejo de datos externos, generacion de reportes HTML, logging y captura automatica de pantalla.

## Tecnologias utilizadas
- Python 3.x
- Pytest
- Selenium WebDriver
- Logging
- Faker
- CSV / JSON
- Request

## Reportes y Logs

El proyecto genera tres tipos principales de resultados durante la ejecucion de las pruebas:
**reporte HTML**, **capturas de pantalla**,
**archivo de log**

### Reporte HTML
Se genera un reporte HTML detallado con el nombre de ```reporte.html``` en la carpeta reports del proyecto

### Logs de ejecución
Tambien se genera un log con información detallada de toda la ejecución de las pruebas en la siguiente ubicacion: ```logs/suite.log```

### Capturas de pantalla

Se realizan capturas de pantalla por cada test que haya fallado y se encuentran en la siguiente ubicacion: ```reports/screens/```

## Ejecutar todas las pruebas
Para iniciar la ejecución de las pruebas debes ejecutar la siguiente linea: 

```bash
python -m run_test-py
```

## ¿Cómo interpretar los reportes?
- Al ejecutar `run_test.py`, se genera un archivo HTML en la carpeta raiz.
- El reporte incluye: 
    - Lista completa de test ejecutados
    - El estado de cada prueba
    - La duración de cada test
    - Las capturas de pantalla para pruebas fallidas

## Pruebas incluidas 
- Login exitoso y fallido
- Login exitoso y fallido usando faker
- Comportamiento de la página del inventario
- Comportamiento de la página del carrito
- API (Reqres): GET users, POST create user, DELETE user, validaciones de código HTTP, validaciones de estructura JSON

## Manejo de datos de pruebas
- En la carpeta `datos` se incluyen archivos como: 
    - `data_login.csv` -> datos de usuarios válidos o inválidos
    - `productos.json` -> datos de productos para validación

## Conclusión 
Este proyecto ofrece una estructura organizada y escalable para automatizar pruebas de API utilizando Python y Pytest. 
Incluye un flujo simple de ejecución mediante `run_test.py`, generacion automatica de reporte HTML facilitando el analisis de las pruebas.

La arquitectura del proyecto esta pensada para agregar nuevos casos de prueba y configuraciones sin modificar el nucleo del proyecto, manteniendo buenas practicas y permitiendo su escalabilidad en el tiempo.

