def socioEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "nombre": item["nombre"],
        "email": item["email"],
        "clave": item["clave"],
    }

def sociosEntity(entity) -> list:
    return [socioEntity(item) for item in entity]