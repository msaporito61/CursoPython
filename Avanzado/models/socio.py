from typing import Optional
from pydantic import BaseModel


class Socio(BaseModel):
    id: Optional[str]
    nombre: str
    email: str
    clave: str

    class Config:
        schema_extra = {
            "example": {
                "nombre": "Juan",
                "email": "juan@mail.com",
                "clave": "secreta"
            }
        }
