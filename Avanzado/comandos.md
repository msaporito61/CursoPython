- Crear el directorio de trabajo

- Ir al directorio de trabajo

- Crear el enviroment de trabajo
    ```sh
    $ python3 -m venv .venv
    ```

- Activar el entorno virtual

    ```sh
    $ source .venv/bin/activate
    (.venv) $
    ```

- Ejecutar el Visual Studio Code

    ```sh
    $ code .
    ```

- Crear un archivo llamado **main.py** e introduzco en siguente codigo:

    ```python
    #!/usr/bin/env python3
    print("Prueba de funcionamiento..")
    ```

- Pruebo la ejecuccion en el entorno

    ```sh
    $ python main.py
    ```

- Instalo el framework **Fastapi**

    ```sh
    $ pip install "fastapi[all]"
    ```

- Instalo el **uvicorn** ASGI Webserver

    ```sh
    $ pip install "uvicorn[standard]"
    ```

- Instalo la conexion para MongoDB
    ```sh
    $ pip install pymongo
    ```

- Modifico el archivo **main.py**

    ```python
    from fastapi import FastAPI

    app = FastAPI()
    ```

- Pruebo la ejecuccion de la aplicacion:

    ```sh
    $ uvicorn main.py

    ERROR:    Error loading ASGI app. Import string "main.py" must be in format "<module>:<attribute>".
    ```
- El error me informa que debo ejecutar la aplicacion:

    ```sh
    $ uvicorn main:app
    ```

- Una vez verificado el funcionamiento procedo a configurar las carpetas de mi proyecto:

    ```sh
    $ mkdir config
    $ mkdir models
    $ mkdir routes
    $ mkdir schemas
    ```
- Dentro de la carpeta **routes** creo el archivo **socio.py**

    ```python 
    from fastapi import APIRouter

    socio = APIRouter()


    @socio.get('/socios')
    def prueba():
        return "Prueba de Funcionamiento"
    ```

- Modifico el archivo **main.py**

    ```python
    from fastapi import FastAPI
    from routes.socio import socio

    app = FastAPI()

    app.include_router(socio)

    ```

- Al realizar los cambios no se ven reflejados en la ejecuccion actual, se debe interrumpir y llamar de la siguiente forma:

    ```sh
    $ uvicorn main:app --reload
    ```

 - Ahora debemos generar el esquema de los datos, para esto creamos un archivo **socio.py** en la carpeta **schema**

    ```python
   def socioEntity(item) -> dict:
    return {
        "id": item["id"],
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }
    ```

- Modifico en la carpeta **routes** el archivo **socio.py**

    ```python
    from fastapi import APIRouter

    socio = APIRouter()

    @socio.get('/socios')
    def find_all_socios():
        return "Prueba de Funcionamiento"

    # Create
    @socio.post('/socios')
    def create_socio():
        return "Prueba de Funcionamiento"

    # Read
    @socio.get('/socios/{id}')
    def find_socio():
        return "Prueba de Funcionamiento"

    # Update
    @socio.put('/socios/{id}')
    def uptdate_socio():
        return "Prueba de Funcionamiento"

    # Delete

    @socio.delete('/socios/{id}')
    def find_socios():
        return "Prueba de Funcionamiento"

    ```

- Verifico en el navegador la documentacion:

    ```sh
    open http://localhost:8000/docs
    ```

- Para poder extraer los datos desde una base de datos, en este caso **MongoDB**, dentro de la carpeta **config** creo un archivo **db.py**

    ```python
    from pymongo import MongoClient

    conn = MongoClient()

    ```

- Creo el modelo de datos a usar con la base de datos, en la carpeta **models** creo un archivo **socio.py**

    ```python
    from typing import Optional
    from pydantic import BaseModel


    class socio(BaseModel):
        id: Optional[str]
        name: str
        email: str
        password: str

    ```

- Modifico el archivo **socio.py** de la carpeta **schemas**

    ```python
    def socioEntity(item) -> dict:
        return {
            "id": item["id"],
            "name": item["name"],
            "email": item["email"],
            "password": item["password"]
        }

    def sociosEntity(entity) -> list:
        return [socioEntity(item) for item in entity]
    ```

- Procedo a abrir el archivo **socio.py** dentro de la carpeta **routes**

    ```python
    from fastapi import APIRouter
    from config.db import conn
    from schemas.socio import socioEntity, sociosEntity
    from models.socio import socio

    socio = APIRouter()


    @socio.get('/socios')
    def find_all_socios():
        return sociosEntity(conn.local.socio.find())

    # Create
    @socio.post('/socios')
    def create_socio(socio: socio):
        new_socio = dict(socio)
        del new_socio["id"]

        id = conn.local.socio.insert_one(new_socio).inserted_id
        
        socio = conn.local.socio.find_one({"_id": id})

        return socioEntity(socio)


    # Read
    @socio.get('/socios/{id}')
    def find_socio():
        return "Prueba de Funcionamiento"

    # Update
    @socio.put('/socios/{id}')
    def uptdate_socio():
        return "Prueba de Funcionamiento"

    # Delete
    @socio.delete('/socios/{id}')
    def find_socios():
        return "Prueba de Funcionamiento"

    ```


- Modifico el esquema 

    ```Python
    def socioEntity(item) -> dict:
        return {
            "id": str(item["_id"]),
            "name": item["name"],
            "email": item["email"],
            "password": item["password"]
        }

    def sociosEntity(entity) -> list:
        return [socioEntity(item) for item in entity]
    ```


- Instalo el modulo de manejos de claves:

```sh
$ pip install passlib
```

- Procedo a abrir el archivo **socio.py** dentro de la carpeta **routes**, para agregar la encriptacion de las claves

    ```python
    from fastapi import APIRouter
    from config.db import conn
    from schemas.socio import socioEntity, sociosEntity
    from models.socio import socio
    from passlib.hash import sha256_crypt
    ...

    # Create
    @socio.post('/socios')
    def create_socio(socio: socio):
        new_socio = dict(socio)
        new_socio["password"] = sha256_crypt.encrypt(new_socio["password"])
        del new_socio["id"]

        id = conn.local.socio.insert_one(new_socio).inserted_id
        
        socio = conn.local.socio.find_one({"_id": id})

        return socioEntity(socio)

    ...
    ```

- Para poder recuperar un solo usuario modifico **socio.py** en **routes**

    ```python
    from fastapi import APIRouter
    from config.db import conn
    from schemas.socio import socioEntity, sociosEntity
    from models.socio import socio
    from passlib.hash import sha256_crypt
    from bson import ObjectId

    ...
    # Read
    @socio.get('/socios/{id}')
    def find_socio(id: str):
        return socioEntity(conn.local.socio.find_one({"_id":ObjectId(id)}))
    ...
    ```


- Para borrar un usuario modifico **socio.py** en la carpeta **routes**

```python
from fastapi import APIRouter, Response
from config.db import conn
from schemas.socio import socioEntity, sociosEntity
from models.socio import socio
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

...
# Delete
@socio.delete('/socios/{id}')
def delete_socio(id: str):
    socioEntity(conn.local.socio.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

...
```

- Para modificar usuarios debo modificar **socio.py** en la carpeta **routes**

```python
...

# Update
@socio.put('/socios/{id}')
def uptdate_socio(id: str, socio: socio):
    modif_socio = dict(socio)
    if modif_socio["password"]:
        modif_socio["password"] = sha256_crypt.encrypt(modif_socio["password"])
    socioEntity(conn.local.socio.find_one_and_update({"_id": ObjectId(id)}, {"$set": modif_socio}))
    return socioEntity(conn.local.socio.find_one({"_id": ObjectId(id)}))
...
```

- Para que las respuestas en la documentacion sean mas legibles debo modificar **socio.py** en la carpeta **routes**

    ```python
    ...
    # List
    @socio.get('/socios', response_model=list[socio], tags=["socios"])
    def find_all_socios():
        return sociosEntity(conn.local.socio.find())
    ...
    # Create
    @socio.post('/socios', response_model=socio, tags=["socios"])
    def create_socio(socio: socio):
        new_socio = dict(socio)
        new_socio["password"] = sha256_crypt.encrypt(new_socio["password"])
        del new_socio["id"]

        id = conn.local.socio.insert_one(new_socio).inserted_id

        socio = conn.local.socio.find_one({"_id": id})

        return socioEntity(socio)

    ...
    # Delete
    @socio.delete('/socios/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["socios"])
    def delete_socio(id: str):
        socioEntity(conn.local.socio.find_one_and_delete({"_id": ObjectId(id)}))
        return Response(status_code=HTTP_204_NO_CONTENT)
    ...

    ```

- Tambien puedo modificar el archivo **main.py**, para aumentar la informacion en la documentacion

    ```python
    from fastapi import FastAPI
    from routes.socio import socio
    from docs import tags_metadata

    app = FastAPI(
        title="REST API del curso de Python con MongoBD",
        description="Este es un ejemplo para el curso usando FastAPI ",
        version="0.0.1",
        openapi_tags=tags_metadata

    )

    app.include_router(socio)
    ```

- Creo el archivo de metadata **docs.py**

```python
tags_metadata = [{
    "name":"socios",
    "description": "socios routes"
}]
```

- Para mas datos en la carpeta **models** el archivo **socio.py**

```python
from typing import Optional
from pydantic import BaseModel


class socio(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password": "password",
            }
        }

```

