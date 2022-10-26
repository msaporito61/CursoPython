from typing import Optional
from pydantic import BaseModel
from config.db import conn
from schemas.cuota import cuotaEntity, cuotasEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from fastapi import Response, status



class Cuota(BaseModel):
    id: Optional[str]
    socio: str
    importe: str
    fecha: str

    class Config:
        schema_extra = {
            "example": {
                "socio": "63569b762d822389564705b1",
                "importe": "1000",
                "fecha": "06/2022",
            }
        }

#Lista
def listar_cuotas():
    return cuotasEntity(conn.club.cuota.find())

#Crear
def crear_cuota(cuota: Cuota):
    nueva_cuota = dict(cuota)
    del nueva_cuota["id"]
    id = conn.club.cuota.insert_one(nueva_cuota).inserted_id
    cuota = conn.club.cuota.find_one({"_id":id})
    return cuotaEntity(cuota)

#Leer una Cuota
def buscar_cuota(id: str):
    return cuotaEntity(conn.club.cuota.find_one({"_id":ObjectId(id)}))

# Modificar una cuota
def modificar_cuota(id: str, cuota:Cuota):
    modif_cuota = dict(cuota)
    del modif_cuota["id"]
    conn.club.cuota.find_one_and_update({"_id":ObjectId(id)}, {"$set":modif_cuota})
    return cuotaEntity(conn.club.cuota.find_one({"_id":ObjectId(id)}))

# Borrar una cuota
def borrar_cuota(id: str):
    conn.club.cuota.find_one_and_delete({"_id":ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)

# Listado de Cuotas de un Socio
def listar_cuota_socio(socio: str):
    return cuotasEntity(conn.club.cuota.find({"socio":socio}))