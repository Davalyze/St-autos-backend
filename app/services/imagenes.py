from app.crud import imagenes as crud_imagenes


# -------------------------------------------------------
# ⭐ 1. Registrar una imagen asociada a un vehículo
# -------------------------------------------------------
def registrar_imagen(vehiculo_id: int, blob_name: str, es_principal: bool):
    """
    Registra una imagen para un vehículo.
    """
    crud_imagenes.crear_imagen(
        vehiculo_id=vehiculo_id,
        blob_name=blob_name,
        es_principal=es_principal
    )

    return {
        "vehiculo_id": vehiculo_id,
        "blob_name": blob_name,
        "es_principal": es_principal
    }


# -------------------------------------------------------
# 📸 2. Obtener todas las imágenes de un vehículo
# -------------------------------------------------------
def obtener_imagenes_vehiculo(vehiculo_id: int):
    rows = crud_imagenes.obtener_imagenes(vehiculo_id)

    if not rows:
        return []

    # Convertimos a un listado limpio
    return [
        {
            "id": r.get("id"),
            "vehiculo_id": r.get("vehiculo_id"),
            "blob_name": r.get("blob_name"),
            "es_principal": r.get("es_principal")
        }
        for r in rows
    ]


# -------------------------------------------------------
# ⭐ 3. Obtener la imagen principal
# -------------------------------------------------------
def obtener_imagen_principal(vehiculo_id: int):
    rows = crud_imagenes.obtener_imagen_principal(vehiculo_id)

    if not rows:
        return None

    r = rows[0]
    return {
        "id": r.get("id"),
        "vehiculo_id": r.get("vehiculo_id"),
        "blob_name": r.get("blob_name"),
        "es_principal": r.get("es_principal")
    }
