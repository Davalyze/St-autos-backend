from app.crud import vehiculos as crud_vehiculos

def crear_vehiculo(data: dict):
    """
    Crea un vehículo completo desde captación.
    """
    row = crud_vehiculos.crear_vehiculo(data)

    if not row:
        return None

    return row

def obtener_vehiculos():
    """
    Obtiene todos los vehículos completos para el catálogo.
    """
    rows = crud_vehiculos.obtener_vehiculos()

    if not rows:
        return []

    return rows

def obtener_vehiculo_por_id(id: int):
    row = crud_vehiculos.obtener_vehiculo_por_id(id)

    if not row:
        return None

    # row viene como lista de dicts porque usamos execute_query
    return row[0]
