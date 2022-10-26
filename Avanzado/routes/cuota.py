from fastapi import APIRouter, Response, status
from models.cuota import Cuota
import models.cuota as mcuota

cuota = APIRouter()

#Lista
@cuota.get('/cuotas', tags=['Cuotas'], response_model=list[Cuota])
def listar_cuotas():
    return mcuota.listar_cuotas()

# Crear Cuota
@cuota.post('/cuotas', tags=['Cuotas'])
def crear_cuota(cuota: Cuota):
    return mcuota.crear_cuota(cuota)

# Leer una cuota
@cuota.get('/cuotas/{id}', tags=['Cuotas'])
def buscar_cuota(id: str):
    return mcuota.buscar_cuota(id)

# Modificar una cuota
@cuota.put('/cuotas/{id}', tags=['Cuotas'])
def modificar_cuota(id: str, cuota:Cuota):
    return mcuota.modificar_cuota(id, cuota)
   

# Borrar una cuota
@cuota.delete('/cuotas/{id}', tags=['Cuotas'], status_code=status.HTTP_204_NO_CONTENT)
def borrar_cuota(id: str):
    return mcuota.borrar_cuota(id)

# Listado de Cuotas de un Socio
@cuota.get('/cuotas/socio/{socio}', tags=['Cuotas'])
def listar_cuota_socio(socio: str):
    return mcuota.listar_cuota_socio(socio)

