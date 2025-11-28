from app.crud import vehiculos as crud_vehiculos
from app.services import a_transformer as transformer 
from app.db.azure_connection import AzureBlobService
azure = AzureBlobService()
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
    df_vehiculos = transformer.sql_to_df(rows)
    if 'blob_name' in df_vehiculos.columns:
        df_vehiculos['imagen_url'] = df_vehiculos['blob_name'].apply(
            lambda x: azure.build_blob_url(x) if x else None
        )
    else:
        df_vehiculos['imagen_url'] = None
    del df_vehiculos['blob_name']
    rows = transformer.df_to_dict(df_vehiculos)

    return rows

def obtener_vehiculo_por_id(id: int):
    rows = crud_vehiculos.obtener_vehiculo_por_id(id)

    if not rows:
        return None

    # ---------------------------------------
    # Extraer datos del vehículo (fila 0)
    # ---------------------------------------
    base = rows[0].copy()

    # Quitamos blob_name porque ahora serán muchas imágenes
    base.pop("blob_name", None)

    # ---------------------------------------
    # Construir lista de TODAS las imágenes
    # ---------------------------------------
    imagenes = []
    for r in rows:
        blob = r.get("blob_name")
        if blob:
            imagenes.append({
                "blob_name": blob,
                "imagen_url": azure.build_blob_url(blob)
            })

    # ---------------------------------------
    # Añadir imágenes al detalle
    # ---------------------------------------
    base["imagenes"] = imagenes

    return base

