from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.socio import socioEntity, sociosEntity
from models.socio import Socio
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

socio = APIRouter()

# Lista
@socio.get("/socios", tags=["Socios"])
def listar_socios():
    return sociosEntity(conn.club.socio.find())


# Crear
@socio.post("/socios", tags=["Socios"])
def crear_socio(socio: Socio):
    nuevo_socio = dict(socio)
    nuevo_socio["clave"] = sha256_crypt.encrypt(nuevo_socio["clave"])
    del nuevo_socio["id"]
    id = conn.club.socio.insert_one(nuevo_socio).inserted_id
    socio = conn.club.socio.find_one({"_id":id})
    return socioEntity(socio)

# Leer un socio
@socio.get("/socios/{id}", tags=["Socios"])
def buscar_socio(id: str):
    return socioEntity(conn.club.socio.find_one({"_id":ObjectId(id)}))


# Modificar un socio
@socio.put("/socios/{id}", tags=["Socios"])
def modificar_socio(id: str, socio: Socio):
    modif_socio = dict(socio)
    modif_socio["clave"] = sha256_crypt.encrypt(modif_socio["clave"])
    del modif_socio["id"]
    conn.club.socio.find_one_and_update({"_id":ObjectId(id)}, {"$set":modif_socio})
    return socioEntity(conn.club.socio.find_one({"_id":ObjectId(id)}))


# Borrar un socio
@socio.delete("/socios/{id}", tags=["Socios"], status_code=status.HTTP_204_NO_CONTENT)
def borrar_socio(id: str):
    conn.club.socio.find_one_and_delete({"_id":ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
