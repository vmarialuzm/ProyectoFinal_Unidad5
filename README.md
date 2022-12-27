# Proyecto final Unidad 5 y Unidad 7

Este proyecto es una API de pagos de servicios.

## Instalación

Para instalar y utilizar este proyecto, siga estos pasos:

1. Clone este repositorio
2. Cree un entorno virtual y actívelo
3. Instale las dependencias del proyecto con `pip install -r requirements.txt`
4. Configure la base de datos en `principal/settings.py`
5. Ejecute `python manage.py migrate` para aplicar las migraciones
6. Inicie el servidor de desarrollo con `python manage.py runserver`

## Uso

Para acceder a la interfaz de usuario, abra `http://localhost:8000/` en su navegador.

Para acceder a las API, puede utilizar Postman. Las API están disponibles en `http://localhost:8000/api/`.

## API

Este proyecto incluye las siguientes API:

- `/api/users/`: una lista de todos los usuarios
- `/api/users/<id>/`: detalles de un usuario en particular
- `/api/posts