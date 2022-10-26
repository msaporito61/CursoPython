def cuotaEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "socio": item["socio"],
        "importe": item["importe"],
        "fecha": item["fecha"],
    }

def cuotasEntity(entity) -> list:
    return [cuotaEntity(item) for item in entity]