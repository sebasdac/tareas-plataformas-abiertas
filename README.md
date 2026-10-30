# Práctica 3 - Métodos HTTP

En esta práctica hice una API sencilla de estudiantes usando Python y Flask. La idea era practicar los métodos HTTP GET, POST, PUT y DELETE, y ver cómo responde cada uno desde Postman.

No utilicé una base de datos porque la práctica solo pide simular las operaciones. Por eso, aunque se envíe un estudiante nuevo o se elimine uno, la lista de ejemplo no cambia.

## Cómo ejecutar el proyecto

Primero hay que tener Python instalado. Después, abrir el proyecto en Visual Studio Code y ejecutar estos comandos en la terminal:

```bash
cd estudiantes
python -m pip install -r requirements.txt
python app.py
```

Si todo está bien, la API queda funcionando en `http://127.0.0.1:5000`.

## Métodos que hice

- **GET `/estudiantes`**: muestra una lista de ejemplo con Ana, Carlos y María.
- **POST `/estudiantes`**: recibe el nombre de un estudiante en JSON y responde que fue agregado.
- **PUT `/estudiantes/1`**: recibe un nombre nuevo en JSON y responde que el estudiante con ID 1 fue actualizado.
- **DELETE `/estudiantes/1`**: responde que el estudiante con ID 1 fue eliminado.

Para el **POST**, se puede enviar este JSON:

```json
{
  "nombre": "Pedro"
}
```

Y para el **PUT**, este:

```json
{
  "nombre": "Pedro Ramírez"
}
```

## Pruebas con Postman

Con la API ejecutándose, se pueden probar las cuatro peticiones en Postman usando la dirección `http://127.0.0.1:5000` y las rutas anteriores.

En POST y PUT hay que entrar a **Body**, seleccionar **raw** y luego **JSON** para enviar el nombre. GET y DELETE no necesitan body.

También dejé una colección de Postman en la carpeta `postman` para no tener que crear las solicitudes una por una.

## Archivos del proyecto

- `estudiantes/app.py`: código de la API.
- `estudiantes/requirements.txt`: dependencia de Flask.
- `postman/`: colección para probar las peticiones.
- `tests/`: pruebas sencillas de los endpoints.

Con esto se cubren los cuatro métodos HTTP pedidos en la práctica sin necesidad de guardar datos realmente.
